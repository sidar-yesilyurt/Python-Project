# data_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:/Users/yesil/Desktop/Python Project/Part 2/messy_dataset.csv")
print("Initial Dataset:")
print(df.head())

# Data Cleaning
# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Sales'].fillna(df['Sales'].mean(), inplace=True)
df['Profit'].fillna(df['Profit'].mean(), inplace=True)
df.dropna(subset=['Gender'], inplace=True)

# Remove duplicates and fix data types
df.drop_duplicates(inplace=True)
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove outliers from Sales
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
df = df[~((df['Sales'] < (Q1 - 1.5 * (Q3-Q1))) | (df['Sales'] > (Q3 + 1.5 * (Q3-Q1))))]

# Data Analysis
sales_summary = df.groupby('Category')['Sales'].sum().reset_index()
df['Profit Margin'] = (df['Profit'] / df['Sales']).fillna(0)

# Show summary statistics and correlations
print("\nSummary Statistics:")
print(df.describe())
print("\nCorrelation Matrix:")
print(df.select_dtypes(include=[np.number]).corr())

# Visualizations
plt.figure(figsize=(10,6))
plt.hist(df['Sales'], bins=20, color='skyblue')
plt.title('Sales Distribution')
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(x='Sales', y='Profit', hue='Category', data=df)
plt.title('Sales vs Profit')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x='Category', y='Sales', data=sales_summary)
plt.title('Total Sales by Category')
plt.show()

# Save cleaned data
df.to_csv(r"C:/Users/yesil/Desktop/Python Project/Part 2/clean_dataset.csv", index=False)
print("\nCleaned dataset saved.")