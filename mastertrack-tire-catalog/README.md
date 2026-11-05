# Mastertrack Tire Catalog

Square-style tire catalog for **Mastertrack**, organized by tire size.

## Contents

- `data/catalog.tsv` — all 280 Mastertrack products
- `data/sizes/` — separate catalog files for 16, 17, 18, 19, 20, 22-inch tires
- `scripts/validate_catalog.py` — validates every TSV file

## Validate

```bash
python scripts/validate_catalog.py
```

Open TSV files with UTF-8 encoding and Tab as the delimiter. Verify price, inventory, location, visibility, and fulfillment fields before importing into a live Square account.
