import sys 
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scraper import scrape_furlenco

try:
    print("Starting scrape_furlenco()...")
    products = scrape_furlenco(limit=5)
    print(f"\n✓ Successfully scraped {len(products)} products!")
    
    if products:
        print("\nFirst product:")
        print(products[0])
    else:
        print("No products found.")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
