from bing_image_downloader import downloader

# Define fruits and ripeness stages
fruit_classes = {
    "Mango": ["Raw", "SemiRipe", "Ripe", "Overripe"],
    "Banana": ["Raw", "SemiRipe", "Ripe", "Overripe"],
    "Apple": ["Raw", "Ripe", "Overripe"],
    "Avocado": ["Raw", "Ripe", "Overripe"],
    "Tomato": ["Raw", "SemiRipe", "Ripe"]
}

# Download images to correct folder
for fruit, stages in fruit_classes.items():
    for stage in stages:
        query = f"{fruit} {stage} fruit"
        output_dir = f"dataset/{fruit}/{stage}"
        print(f"📥 Downloading: {query} → {output_dir}")
        downloader.download(query, limit=30, output_dir="dataset", adult_filter_off=True, force_replace=False, timeout=60)

print("✅ All images downloaded and saved into dataset folders!")
