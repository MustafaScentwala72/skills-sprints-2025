import pandas as pd

# create a small dataset like excel
data = {
    "Name": ["Aisha", "Ben", "Caro", "Drew"],
    "Country": ["UK", "UK", "IN", "IN"],
    "Spend": [350, 120, 200, 0]
}

df = pd.DataFrame(data)

print("=== Our dataset ===")
print(df)

# 1) basic info about the dataset
print("\n=== Info ===")
print(df.info())

# 2) summary statistics (like avg, min, max)
print("\n=== Summary ===")
print(df.describe())

# 3) total spend grouped by country
print("\n=== Total spend by country ===")
print(df.groupby("Country")["Spend"].sum())

# 4) add a new column: high spender flag
df["HighSpender"] = df["Spend"] > 150
print("\n=== With HighSpender flag ===")
print(df)
