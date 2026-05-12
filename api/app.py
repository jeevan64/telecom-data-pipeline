from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load processed data
df = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\telecom_data_pipeline\data\processed\final_spark_output.csv"
)

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.get("/top-customers")
def top_customers():
    top = df.sort_values(by="total_usage", ascending=False).head(5)
    return top.to_dict(orient="records")

@app.get("/total-revenue")
def total_revenue():
    total = df["revenue"].sum()
    return {"total_revenue": float(total)}

@app.get("/usage-by-city")
def usage_by_city():
    result = df.groupby("city")["total_usage"].sum().reset_index()
    return result.to_dict(orient="records")