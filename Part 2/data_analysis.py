"By Sidar Yesilyurt; Handle and work with data from CSV files."


# data_analysis.py
# This script cleans and analyzes a messy dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"Part 2/messy_dataset.csv")
print("Initial Dataset:")
print(df.head())  # Show first few rows

# ------------
# Data Cleaning
# ------------
# Fill the missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Sales'].fillna(df['Sales'].mean(), inplace=True)
df['Profit'].fillna(df['Profit'].mean(), inplace=True)
df.dropna(subset=['Gender'], inplace=True)  # Remove rows with missing Gender

# Remove duplicates 
df.drop_duplicates(inplace=True)

# Fix data types
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')  # Convert to numbers
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert to dates

# Remove outliers using IQR method
Q1 = df['Sales'].quantile(0.25)  # First quartile
Q3 = df['Sales'].quantile(0.75)  # Third quartile
IQR = Q3 - Q1
df = df[~((df['Sales'] < (Q1 - 1.5 * IQR)) | (df['Sales'] > (Q3 + 1.5 * IQR)))]

# ------------
# Data Analysis
# ------------
# Group sales by category
sales_summary = df.groupby('Category')['Sales'].sum().reset_index()

# Calculate Profit Margin
df['Profit Margin'] = (df['Profit'] / df['Sales']).fillna(0)

# Show summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Show correlation between numerical columns
print("\nCorrelation Matrix:")
print(df.select_dtypes(include=[np.number]).corr())

# ------------
# Visualizations
# ------------
# Histogram of Sales
plt.figure(figsize=(10,6))
plt.hist(df['Sales'], bins=20, color='skyblue')
plt.title('Sales Distribution')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of Sales vs Profit
plt.figure(figsize=(10,6))
sns.scatterplot(x='Sales', y='Profit', hue='Category', data=df)
plt.title('Sales vs Profit')
plt.show()

# Bar chart of Sales by Category
plt.figure(figsize=(10,6))
sns.barplot(x='Category', y='Sales', data=sales_summary)
plt.title('Total Sales by Category')
plt.show()

# Save cleaned data
df.to_csv(r"Part 2/clean_dataset.csv", index=False)
print("\nCleaned dataset saved.")