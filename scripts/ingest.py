import pandas as pd

print("Loading data...")

customers = pd.read_csv("data/raw/customers.csv")
usage = pd.read_csv("data/raw/usage.csv")
recharge = pd.read_csv("data/raw/recharge.csv")

print("Cleaning data...")

customers.dropna(inplace=True)
usage.dropna(inplace=True)
recharge.dropna(inplace=True)

customers['signup_date'] = pd.to_datetime(customers['signup_date'])
usage['usage_date'] = pd.to_datetime(usage['usage_date'])
recharge['recharge_date'] = pd.to_datetime(recharge['recharge_date'])

print("Saving cleaned data...")

customers.to_csv("data/processed/customers_clean.csv", index=False)
usage.to_csv("data/processed/usage_clean.csv", index=False)
recharge.to_csv("data/processed/recharge_clean.csv", index=False)

print("Done")