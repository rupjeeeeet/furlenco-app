def chunk_product(product):
    chunks = []

    # Main chunk
    base = f"""
    Title: {product.title}
    Price: {product.price}
    Category: {product.category}
    Description: {product.description}
    """

    chunks.append(base.strip())

    # Features chunk
    if product.features:
        feat = "Features:\n" + "\n".join(product.features)
        chunks.append(feat.strip())

    return chunks
