from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import re

BASE_URL = "https://www.furlenco.com"


# ------------------------- PRICE CLEANER ------------------------- #
def clean_price(price):
    if not price or not isinstance(price, str):
        return None
    
    price = price.replace("₹", "").replace("Rs", "").replace(",", "").strip()
    price = re.sub(r"[^0-9.]", "", price)

    if not price:
        return None

    try:
        result = float(price)
        if 100 < result < 1000000:
            return result
        return None
    except Exception:
        return None


# ------------------------- FEATURE PARSER ------------------------- #
def extract_features(soup):
    features = {}

    # Each feature row is inside: <div class="MuiBox-root ...">
    spec_blocks = soup.select("div.MuiBox-root")

    for block in spec_blocks:
        p_tags = block.find_all("p")

        # Most blocks contain EXACTLY 2 p-tags → label + value
        if len(p_tags) == 2:
            key = p_tags[0].get_text(" ", strip=True).rstrip(":")
            val = p_tags[1].get_text(" ", strip=True)
            if key and val:
                features[key] = val

    return features


# ------------------------- SINGLE PRODUCT SCRAPER ------------------------- #
def scrape_single_product(page, url):
    page.goto(url, wait_until="load")
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")

    # ------------------------- TITLE ------------------------- #
    title_tag = soup.select_one("h1, h2.MuiTypography-root")
    title = title_tag.get_text(strip=True) if title_tag else None

    # ------------------------- PRICE ------------------------- #
    price = None
    for tag in soup.find_all(["span", "div", "p", "strong", "b"]):
        text = tag.get_text(strip=True)
        if "₹" in text or text.startswith("Rs"):
            cleaned = clean_price(text)
            if cleaned:
                price = cleaned
                break

    # ------------------------- DESCRIPTION ------------------------- #
    description = None
    possible_descs = soup.select("p.MuiTypography-root, div.MuiTypography-root")

    for tag in possible_descs:
        txt = tag.get_text(" ", strip=True)
        if len(txt) > 40:  # avoid short labels
            description = txt
            break

    # Fallback keyword-based extraction
    if not description:
        for p in soup.find_all("p"):
            txt = p.get_text(" ", strip=True)
            if any(k in txt.lower() for k in ["wood", "design", "finish", "support", "crafted"]):
                description = txt
                break

    # ------------------------- IMAGES ------------------------- #
    images = []
    for img in soup.select("img"):
        src = img.get("src")
        if src:
            images.append(urljoin(BASE_URL, str(src)))

    # ------------------------- FEATURES ------------------------- #
    features = extract_features(soup)

    return {
        "url": url,
        "title": title,
        "price": price,
        "description": description,
        "images": list(set(images)),
        "features": features,
    }


# ------------------------- CATEGORY SCRAPER ------------------------- #
def scrape_furlenco(limit=30):
    category_url = (
        "https://www.furlenco.com/bengaluru/bedroom-furniture-on-rent"
        "?collectionType=CATEGORY_RENT"
    )

    products = []
    product_urls = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Set location cookie
        context.add_cookies([{
            "name": "location",
            "value": "bengaluru",
            "domain": ".furlenco.com",
            "path": "/"
        }])

        page = context.new_page()

        print(f"Loading: {category_url}")
        page.goto(category_url, wait_until="load", timeout=120000)
        time.sleep(3)  # Allow JS to render content

        soup = BeautifulSoup(page.content(), "html.parser")

        # Extract product URLs
        product_links = soup.select("a[href*='/products/']")
        print(f"Found {len(product_links)} links")

        for link in product_links:
            href = link.get("href")
            if href and "/products/" in href:
                full_url = urljoin(BASE_URL, str(href))
                if full_url not in product_urls:
                    product_urls.append(full_url)

            if len(product_urls) >= limit:
                break

        print(f"Scraping {len(product_urls)} products...")

        # Scrape each product page
        for idx, url in enumerate(product_urls):
            try:
                print(f"[{idx+1}/{len(product_urls)}] Scraping {url}")
                data = scrape_single_product(page, url)

                if data.get("title"):
                    products.append(data)
                    print(f"  ✓ {data['title'][:60]}")
                else:
                    print(f"  ⚠ Failed to extract title")

            except Exception as e:
                print(f"  ✗ Error: {e}")

        browser.close()

    return products
