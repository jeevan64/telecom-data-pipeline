import pandas as pd

# Load cleaned data
customers = pd.read_csv("data/processed/customers_clean.csv")
usage = pd.read_csv("data/processed/usage_clean.csv")
recharge = pd.read_csv("data/processed/recharge_clean.csv")

# Merge data
df = customers.merge(usage, on="customer_id")
df = df.merge(recharge, on="customer_id")

# Create new column (business logic)
df['total_usage'] = df['call_minutes'] + df['data_mb']
df['revenue'] = df['amount']

# Save final output
df.to_csv("data/processed/final_output.csv", index=False)

print("Transformation complete")