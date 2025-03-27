from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# Load Sales Data
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Ensure the 'static' folder exists for saving images
if not os.path.exists("static"):
    os.makedirs("static")

# 📊 Generate Sales Trend Plot
def generate_sales_trend():
    daily_sales = df.groupby("Date")["Total Sales"].sum()
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=daily_sales.index, y=daily_sales.values, marker="o", color="b")
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Sales (€)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig("static/sales_trend.png")  # Save the plot
    plt.close()

# 📊 Generate Top 5 Best-Selling Products Plot
def generate_top_products():
    top_products = df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
    plt.title("Top 5 Best-Selling Products")
    plt.xlabel("Total Sales (€)")
    plt.savefig("static/top_products.png")
    plt.close()

# 📊 Generate Sales by Category Plot
def generate_sales_by_category():
    sales_by_category = df.groupby("Category")["Total Sales"].sum()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=sales_by_category.values, y=sales_by_category.index, palette="coolwarm")
    plt.title("Sales by Category")
    plt.xlabel("Total Sales (€)")
    plt.savefig("static/sales_by_category.png")
    plt.close()

@app.route("/")
def dashboard():
    # Generate the latest visualizations before rendering the page
    generate_sales_trend()
    generate_top_products()
    generate_sales_by_category()

    # Calculate summary statistics
    total_sales = df["Total Sales"].sum()
    avg_sales_per_day = df.groupby("Date")["Total Sales"].sum().mean()
    top_products = df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False).head(5)
    sales_by_category = df.groupby("Category")["Total Sales"].sum()

    return render_template("dashboard.html",
                           total_sales=total_sales,
                           avg_sales_per_day=avg_sales_per_day,
                           top_products=top_products.to_dict(),
                           sales_by_category=sales_by_category.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
