import os

from datasets import load_dataset

os.makedirs("data", exist_ok=True)  # data/ is git-ignored at the repo root

# A bigger dataset than the 500-row sample: 25,000 IMDB reviews (~84 MB download)
ds = load_dataset("stanfordnlp/imdb", split="train")

# --- Exercise 3: CSV vs Parquet ---
ds.to_csv("data/imdb_train.csv")
ds.to_parquet("data/imdb_train.parquet")
csv_mb = os.path.getsize("data/imdb_train.csv") / 1e6
pq_mb = os.path.getsize("data/imdb_train.parquet") / 1e6
print(f"CSV: {csv_mb:.1f} MB | Parquet: {pq_mb:.1f} MB | {csv_mb / pq_mb:.1f}x smaller")

# --- Exercise 4: 70 / 15 / 15 split with a fixed seed ---
first = ds.train_test_split(test_size=0.30, seed=42)  # 70% train, 30% rest
second = first["test"].train_test_split(
    test_size=0.50, seed=42
)  # split the 30% in half

train, val, test = first["train"], second["train"], second["test"]
print(
    f"Train {len(train)} | Val {len(val)} | Test {len(test)} | "
    f"Sum {len(train) + len(val) + len(test)} of {len(ds)}"
)
print("First train label:", train[0]["label"], "| text:", train[0]["text"][:60])
