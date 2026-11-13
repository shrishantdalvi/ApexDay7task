import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import time

#Loading dataset csv file
df = pd.read_csv("Sample - Superstore.csv",encoding="latin1")

#Displaying first and last 10records
print(df.head(10))
print(df.tail(10))

#displaying dataset information and statistics
print(df.info())
print(df.describe())

#Displaying columns and its datatypes
print(df.dtypes)

#Finding missing values and removing missing values
print("missing values:\n",df.isnull().sum())   #No missing values

#Finding dupicated rows and removing duplicated rows
print("Duplicated rows:\n",df.duplicated().sum())  #No duplicated records

#finding unique values from categorical columns
print("Segments:\n",df["Segment"].unique())
print("Country:\n",df["Country"].unique())
print("City:\n",df["City"].unique())
print("State:\n",df["State"].unique())
print("Region:\n",df["Region"].unique())
print("Category:\n",df["Category"].unique())
print("Sub-Category:\n",df["Sub-Category"].unique())

#Removing extraspaces from columns
df.columns = df.columns.str.strip()
print("After removing Extraspaces:\n",df.columns)

#checking invalid and inconsistent data
print("Invalid Sales:",df[df["Sales"] < 0].shape[0])
print("Invalid Quantity:",df[df["Quantity"] < 0].shape[0])
print("Invalid Sales:",df[(df["Discount"] < 0) | (df["Discount"] > 1)].shape[0])

# Convert Order Date
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%Y", errors="coerce"
)

# Convert Ship Date
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%m/%d/%Y", errors="coerce"
)

#displaying dates in date-month-year format 
print(df["Order Date"].dt.strftime("%d-%m-%Y").head(10))
print(df["Ship Date"].dt.strftime("%d-%m-%Y").head(10))

#verifying datatypes and missing values
print(df[["Order Date", "Ship Date"]].dtypes)

print("Missing Order Date:", df["Order Date"].isna().sum())
print("Missing Ship Date:", df["Ship Date"].isna().sum())

#checking inconsistencies
invalid_dates = df[df["Ship Date"] < df["Order Date"]]

print("Invalid Date Records:", invalid_dates.shape[0])

#Total Sales 
Total_sales = df["Sales"].sum()
print("Total Sales:- ",Total_sales)

#Total Profit
Total_profit = df["Profit"].sum()
print("Total Profit:- ",Total_profit)

#Average Sales
Avg_sales = df["Sales"].mean()
print("Average Sales:- ",Avg_sales)

#Average Profit
Avg_profit = df["Profit"].mean()
print("Average Sales:- ",Avg_profit)

#Total orders
Total_orders = df["Order ID"].nunique()
print("Total Orders:- ",Total_orders)

#Number  of Unique customers
uniqu_customers = df["Customer ID"].nunique()
print("Number of unique Customers:- ",uniqu_customers)

#Number of Products solds
product_sold = df["Quantity"].sum()
print("Total Number of Products sold:- ",product_sold)

#Best selling Product
Best_selling_product = df.groupby("Product Name")["Quantity"].max().idxmax()
print("Best Selling Product:- ",Best_selling_product)

#Heighest  revenue Category
Highest_category_sales = df.groupby("Category")["Sales"].sum()
Highest_category = Highest_category_sales.idxmax()
print("Highest revenue Category:- ",Highest_category)

#Top10 customers by sales
Top10_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("Top10 Customers by sales:- ",Top10_customers)

#top5 cities
top5_cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head()
print("Top5 cities:- ",top5_cities)

#Display number of Order gretaer then 1000
orders = df[df["Sales"] > 1000]
count_order = orders.shape[0]
print("Number of Orders Greater then 1000:- ",count_order)

#Display/Filter data for West Region
filtr = df[df["Region"] == "West"]
count_data = filtr.shape[0]
print("Data for West Region:- ",count_data)

#Number of Products above the avg Profit 
Above_avg_profit = df[df["Profit"] > Avg_profit]
print("Profir Above the Average:- ",Above_avg_profit)

#Top Performing month
Monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
topmonth = Monthly_sales.idxmax()
print("The Top Performing Month is:- ",topmonth)

#Display Total Sales by Region
Sales_region = df.groupby("Region")["Sales"].sum()
print("Total Sales by Regions:- ",Sales_region)

#Display Total Profit by category
profit_category = df.groupby("Category")["Profit"].sum()
print("Total Profit by category:- ",profit_category)

#Montly Sales
monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
print("Monthly Sales:- ",monthly_sales)

#Customer Wise revenue
customer_revenue = df.groupby("Customer Name")["Sales"].sum()
print("Customer wise Revenue:- ",customer_revenue)

#product wise quantity sold
Product_quantity = df.groupby("Product Name")["Quantity"].sum()
print("Quantity Sold by Product:- ",Product_quantity)


#Data Visualisation

#Monthly Sales Trend
monthly_sales.index = monthly_sales.index.to_timestamp()
plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index,monthly_sales.values,
         color ="#35B6F6",
         linewidth =2.8,
         marker = "o",
         markersize =5,
         markerfacecolor = "#20D6B0",
         markeredgecolor = "white",
         label = "Monthly Sales")
         
plt.title("Monthly Sales Trend",fontsize=16,fontweight="bold")
plt.xlabel("Months",fontsize=12,fontweight="bold")
plt.ylabel("Sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.grid(axis="y", color="#64748B", linestyle="--", linewidth=0.7, alpha=0.25)

plt.title("Monthly Sales Trend", color="white", fontsize=16, fontweight="bold")
plt.xlabel("Months", color="#38BDF8")
plt.ylabel("Sales", color="#38BDF8")
plt.tick_params(colors="#DCEBFA")


plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.tick_params(colors="#DCEBFA")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Sales by Category bar chart
Sales_category = df.groupby("Category")["Sales"].sum()
plt.bar(Sales_category.index,
        Sales_category.values,
         color="#4C78A8",
         edgecolor="#3A3A3A",
         linewidth=1.2)

plt.title("Total Sales by Category",
          fontsize=16,
          fontweight="bold",
          pad=15)
plt.xlabel("Category",fontsize=12,fontweight="bold")
plt.ylabel("Total Sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)

plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.grid(axis="y", color="#64748B", linestyle="--", linewidth=0.7, alpha=0.25)


plt.title("Monthly Sales Trend", color="white", fontsize=16, fontweight="bold")
plt.xlabel("Months", color="#38BDF8")
plt.ylabel("Sales", color="#38BDF8")
plt.tick_params(colors="#DCEBFA")
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()

#Top10 customers by sales
plt.figure(figsize=(12, 7))

bars = plt.barh(
    Top10_customers.index,
    Top10_customers.values,
    color="#A78BFA",
    height=0.65,
    edgecolor="white",
    linewidth=0.7
)


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.title("TOP 10 CUSTOMERS BY SALES",
          fontsize=16, fontweight="bold", color="white", pad=20)

plt.xlabel("Total Sales (USD)", fontsize=12, color="#38BDF8",
           fontweight="bold")
plt.ylabel("Customer Name", fontsize=12, color="#38BDF8",
           fontweight="bold")


for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2,
             f"${width:,.0f}",
             va="center", ha="left",
             color="white", fontsize=9, fontweight="bold")


plt.grid(axis="x", color="#64748B",
         linestyle="--", linewidth=0.7, alpha=0.25)

plt.gca().set_axisbelow(True)
plt.gca().set_xlim(0, Top10_customers.max() * 1.18)

plt.tick_params(colors="#DCEBFA")

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_color("#3B82F6")
plt.gca().spines["bottom"].set_color("#3B82F6")

plt.tight_layout()
plt.show()