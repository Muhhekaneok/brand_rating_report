import csv
from typing import Iterator


def read_items_from_csv(files: list[str]) -> Iterator[dict]:
    for file_path in files:
        try:
            with open(file_path, mode="r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    try:
                        row["rating"] = float(row["rating"])
                        row["price"] = float(row["price"])
                        yield row
                    except ValueError as e:
                        print(f"Incorrect data in {file_path}: {row}. Error: {e}")
        except FileNotFoundError:
            print(f"File {file_path} not found. Skipping.")
        except Exception as e:
            print(f"An unexpected error occurred with file {file_path}: {e}")
