#!/usr/bin/env python3
import csv
from pathlib import Path
import sys

files = [Path("data/catalog.tsv"), *sorted(Path("data/sizes").glob("*.tsv"))]
failed = False
for path in files:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        rows = csv.reader(source, delimiter="\t")
        header = next(rows, [])
        count = 0
        for line_number, row in enumerate(rows, start=2):
            count += 1
            if len(row) != len(header):
                print(f"{path}: line {line_number} has {len(row)} columns; expected {len(header)}")
                failed = True
    print(f"{path}: {count:,} rows, {len(header)} columns")
sys.exit(1 if failed else 0)
