# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plot style for better visuals
sns.set_style("whitegrid")

# Task 1: Load and Explore the Dataset
# Error handling for file loading
try:
    # Load the dataset
    df = pd.read_csv('swiggy_all_menus_india.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File 'swiggy_all_menus_india.csv' not found. Please ensure the file is in the correct directory.")
    exit()
except Exception as e:
    print(f"Error occurred while loading the dataset: {e}")
    exit()

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Explore the structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset: Drop rows with missing values in critical columns
df_cleaned = df.dropna(subset=['Price (INR)', 'Category', 'Dish Name'])
print("\nDataset shape after dropping missing values:", df_cleaned.shape)

# Task 2: Basic Data Analysis
# Compute basic statistics for numerical columns
print("\nBasic Statistics for Numerical Columns:")
print(df_cleaned[['Price (INR)', 'Rating', 'Rating Count']].describe())

# Group by Category and compute mean Price and Rating
category_stats = df_cleaned.groupby('Category')[['Price (INR)', 'Rating']].mean().reset_index()
print("\nMean Price and Rating by Category:")
print(category_stats.head(10))

# Findings
print("\nFindings from Analysis:")
print("- The dataset contains a variety of dishes with prices ranging from very low to high (as seen in the describe output).")
print("- Categories like 'Recommended' or premium categories may have higher average prices.")
print("- Ratings vary across categories, with some having higher average ratings, indicating popularity or quality.")

# Task 3: Data Visualization
# Create a directory for saving plots
if not os.path.exists('plots'):
    os.makedirs('plots')

# 1. Line Chart: Average Price trend across top 10 categories (sorted by price)
top_categories = category_stats.sort_values('Price (INR)', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.plot(top_categories['Category'], top_categories['Price (INR)'], marker='o')
plt.title('Average Price Trend Across Top 10 Categories', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Average Price (INR)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/line_chart_avg_price.png')
plt.show()

# 2. Bar Chart: Average Rating by Category for top 10 categories
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Rating', data=top_categories)
plt.title('Average Rating by Category (Top 10)', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Average Rating (0-5)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/bar_chart_avg_rating.png')
plt.show()

# 3. Histogram: Distribution of Price (INR)
plt.figure(figsize=(10, 6))
plt.hist(df_cleaned['Price (INR)'], bins=30, edgecolor='black')
plt.title('Distribution of Dish Prices', fontsize=14)
plt.xlabel('Price (INR)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('plots/histogram_price.png')
plt.show()

# 4. Scatter Plot: Price vs Rating
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['Price (INR)'], df_cleaned['Rating'], alpha=0.5)
plt.title('Price vs Rating of Dishes', fontsize=14)
plt.xlabel('Price (INR)', fontsize=12)
plt.ylabel('Rating (0-5)', fontsize=12)
plt.tight_layout()
plt.savefig('plots/scatter_price_vs_rating.png')
plt.show()
