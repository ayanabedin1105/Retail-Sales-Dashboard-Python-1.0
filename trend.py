import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Sales Data
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Aggregate Sales by Date
daily_sales = df.groupby("Date")["Total Sales"].sum()

# Top 5 Best-Selling Products
top_products = df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False).head(5)

# Sales by Category
sales_by_category = df.groupby("Category")["Total Sales"].sum()

# 📊 Plot 1: Sales Trend Over Time
plt.figure(figsize=(10, 5))
sns.lineplot(x=daily_sales.index, y=daily_sales.values, marker="o", color="b")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales (€)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 📊 Plot 2: Top 5 Best-Selling Products
plt.figure(figsize=(8, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 5 Best-Selling Products")
plt.xlabel("Total Sales (€)")
plt.show()

# 📊 Plot 3: Sales by Category
plt.figure(figsize=(8, 5))
sns.barplot(x=sales_by_category.values, y=sales_by_category.index, palette="coolwarm")
plt.title("Sales by Category")
plt.xlabel("Total Sales (€)")
plt.show()

# 📊 Summary Statistics
print("\n📈 Sales Summary:")
print(f"Total Sales: €{df['Total Sales'].sum():,.2f}")
print(f"Average Sales Per Day: €{daily_sales.mean():,.2f}")
print("Best-Selling Products:\n", top_products)
print("Sales by Category:\n", sales_by_category)
