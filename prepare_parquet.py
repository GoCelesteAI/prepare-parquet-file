"""prepare_parquet.py — convert a CSV to Parquet, three ways.

Compares pandas, pyarrow, and polars side-by-side on the same input CSV.

Run:
  python prepare_parquet.py
"""
import os
import pandas as pd
import pyarrow.csv as pa_csv
import pyarrow.parquet as pq
import polars as pl

CSV = "prices.csv"

# 1. pandas
pd.read_csv(CSV).to_parquet("prices_pandas.parquet")

# 2. pyarrow
pq.write_table(pa_csv.read_csv(CSV), "prices_pyarrow.parquet")

# 3. polars
pl.read_csv(CSV).write_parquet("prices_polars.parquet")

# Compare sizes on disk
print("=== Output size on disk ===")
for path in [CSV, "prices_pandas.parquet", "prices_pyarrow.parquet", "prices_polars.parquet"]:
  size = os.path.getsize(path)
  print(f"  {path:<28} {size:>10,} bytes  ({size/1024/1024:.2f} MB)")
