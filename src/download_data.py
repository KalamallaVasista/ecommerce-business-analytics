from pathlib import Path

import kagglehub


DATASET_HANDLE = "olistbr/brazilian-ecommerce"

EXPECTED_FILES = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
]

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def download_dataset() -> None:
    """Download and verify the required Olist dataset files."""

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading Olist e-commerce dataset...")
    kagglehub.dataset_download(
        DATASET_HANDLE,
        output_dir=str(RAW_DATA_DIR),
    )

    missing_files = [
        file_name
        for file_name in EXPECTED_FILES
        if not (RAW_DATA_DIR / file_name).exists()
    ]

    if missing_files:
        raise FileNotFoundError(
            f"Missing required dataset files: {missing_files}"
        )

    print("\nDataset downloaded and verified successfully.")
    print(f"Dataset location: {RAW_DATA_DIR}")
    print(f"Required CSV files found: {len(EXPECTED_FILES)}\n")

    for file_name in EXPECTED_FILES:
        file_path = RAW_DATA_DIR / file_name
        size_mb = file_path.stat().st_size / (1024 * 1024)
        print(f"{file_name}: {size_mb:.2f} MB")


if __name__ == "__main__":
    download_dataset()