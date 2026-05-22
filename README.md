# How to Prepare a Parquet File in Python — Tutorial

> Parquet is the columnar binary format that compresses three to ten times smaller than CSV, reads faster, and preserves the schema in the file.


📺 **Watch:** https://www.youtube.com/watch?v=lr7WtJ9uHSA  
📖 **Article:** https://www.codegiz.com/blog/prepare-parquet-file/  
🎓 **Tutorial + quiz:** https://www.codegiz.com/watch/prepare-parquet-file/

Part of the **Common Questions in Python** series — short, search-targeted answers to the questions Python data folks actually type into YouTube.

---

## What you'll learn

- Parquet is a columnar binary format.
- Pandas is the path of least resistance.
- PyArrow is the lowest layer and gives you full control.
- Polars writes the smallest file by default.
- Schema preservation is the quiet killer feature.

---

## Setup

This demo runs on Python 3.10+ and pandas 2.0+. The other dependencies are installed via the included `requirements.txt`.

```bash
# 1. Clone
git clone https://github.com/GoCelesteAI/prepare-parquet-file.git
cd prepare-parquet-file

# 2. Virtual environment
python3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Run it

```bash
python prepare_parquet.py
```

---

## The code

Here's `prepare_parquet.py` in full — it's deliberately short. The video walks through what each block does.

```python
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
```

---

## Why this exists

Most pandas tutorials are written for the curriculum reader who starts at chapter 1. Real working analysts find pandas through search — `"how do I X in pandas"` typed into Google or YouTube. This series answers each of those questions as a self-contained 4–6 minute single, with a runnable demo you can copy, paste, and adapt to your own data.

---

🤖 *Channel run by Claude AI. Tutorials AI-produced; reviewed and published by Codegiz.* More: [codegiz.com](https://codegiz.com) · [@GoCelesteAI on YouTube](https://www.youtube.com/@GoCelesteAI)
