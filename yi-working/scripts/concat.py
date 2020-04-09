from pathlib import Path
import pandas as pd

data_dir = Path("data")

csv_files = [file for file in (data_dir / "raw_data").iterdir() if ".csv" in str(file)]
df = pd.concat([
    pd
    .read_csv(file)
    .assign(source=str(file).strip(".csv"))
    for file in csv_files
])

df.to_csv(data_dir / "hfea-ivf.csv", index=False)
