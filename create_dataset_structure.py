import os

base_path = "dataset"

fruit_classes = {
    "Apple": ["Fresh", "Rotten", "Unripe"],
    "Banana": ["Fresh", "Rotten", "Unripe"],
    "Mango": ["Fresh", "Rotten", "Unripe"]
}

for fruit, stages in fruit_classes.items():
    for stage in stages:
        path = os.path.join(base_path, fruit, stage)
        os.makedirs(path, exist_ok=True)
        print(f"✅ Created: {path}")
