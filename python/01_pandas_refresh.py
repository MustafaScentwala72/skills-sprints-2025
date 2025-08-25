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

# 5) Only UK rows
uk = df[df["Country"] == "UK"]
print("\n=== UK only ===")
print(uk)

# 6) Average spend across all customers
print("\n=== Average spend ===")
print(df["Spend"].mean())

# 7) Top spender (name + amount)
top = df.loc[df["Spend"].idxmax(), ["Name", "Spend"]]
print("\n=== Top spender ===")
print(top.to_string(index=False))

# ---- extras to learn by doing ----
import os

# A) totals & averages by country
country_totals = df.groupby("Country")["Spend"].sum()
country_avg = df.groupby("Country")["Spend"].mean()
print("\n=== Totals by Country ===")
print(country_totals)
print("\n=== Average Spend by Country ===")
print(country_avg)

# B) simple customer segmentation (bucket)
def bucket(spend):
    if spend > 250: 
        return "High"
    elif spend > 100: 
        return "Medium"
    else:
        return "Low"

df["SpendBucket"] = df["Spend"].apply(bucket)
print("\n=== With SpendBucket ===")
print(df.sort_values("Spend", ascending=False))

# C) export results (so you can hand them to someone else)
os.makedirs("data/outputs", exist_ok=True)
df.to_csv("data/outputs/customers_with_buckets.csv", index=False)
country_totals.to_csv("data/outputs/country_totals.csv")
country_avg.to_csv("data/outputs/country_avg.csv")
print("\nSaved files in data/outputs/")
