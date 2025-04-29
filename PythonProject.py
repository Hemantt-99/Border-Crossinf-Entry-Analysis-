#Python Project

import pandas as pd;
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, ttest_1samp, ttest_ind, ttest_rel

# Load dataset
df = pd.read_csv("Border_Crossing_Entry_Data_final.csv", dtype={'column_name': str}, low_memory=False)

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print(df.columns)

# Read data with low_memory fix
df = pd.read_csv("Border_Crossing_Entry_Data_final.csv", low_memory=False)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# View actual column names and a few date examples
print("Columns:", df.columns)
print(" Sample Dates:", df['date'].unique()[:10])

# Convert date safely
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')

# Report invalid dates
invalid_count = df['date'].isnull().sum()
print(f"⚠️ Invalid dates: {invalid_count}")
# ----------------------------------------------------------------------------

#BASIC INFO 

'''#Display the first 5 rows of the dataset
print(df.head(5))

# Get a concise summary of the dataframe
print(df.info())

# Show basic descriptive statistics
print(df.describe())
print(df.describe(include='all'))

# Check for missing values in each column
print(df.isnull().sum())

# Check column names and types
print(df.dtypes)'''

#-----------------------------------------------------------------------------

#Remove duplicate rows (keep the first occurrence)

'''before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]

print(f"\n Removed {before - after} duplicate rows.")'''

#-----------------------------------------------------------------------------

# Handle missing (NULL) values
'''print("\n--- Missing values BEFORE cleaning ---")
print(df.isnull().sum())

# Strategy: Drop rows with any NULLs (only if data loss is acceptable)
# You could also fill with defaults if needed (see bottom)
df.dropna(inplace=True)

# Recheck missing values
print("\n--- Missing values AFTER cleaning ---")
print(df.isnull().sum())

# Final shape of dataset
print(f"\n Final shape of dataset: {df.shape}")'''


#-----------------------------------------------------------------------------

# Statistical Analysis & Insights

# Summary statistics of numeric columns

'''print("\n--- Summary Statistics (Numerical Columns) ---")
print(df.describe())

# Summary statistics of all columns (including categorical)

print("\n--- Summary Statistics (All Columns) ---")
print(df.describe(include='all'))

# Unique values in key categorical columns\

print("\n--- Unique Ports and Measures ---")
print("Unique Ports:", df['port_name'].nunique())
print("Unique Measures:", df['measure'].nunique())

# Most frequent values (mode) for categorical data

print("\n--- Most Common Entries ---")
print("Most Common Port:", df['port_name'].mode()[0])
print("Most Common Measure:", df['measure'].mode()[0])

# Correlation between numeric columns (if more than one numeric column exists)

print("\n--- Correlation Matrix (Numerical Columns) ---")
print(df.corr(numeric_only=True))

# Top 5 Ports with the Highest Total Value

print("\n--- Top 5 Ports by Total Crossings ---")
top_ports = df.groupby('port_name')['value'].sum().sort_values(ascending=False).head(5)
print(top_ports)

# Top 5 Measures with the Highest Total Value

print("\n--- Top 5 Measures by Total Crossings ---")
top_measures = df.groupby('measure')['value'].sum().sort_values(ascending=False).head(5)
print(top_measures)'''


#-----------------------------------------------------------------------------

#Exploratory Data Analysis (EDA)

df['date'] = pd.to_datetime(df['date'])

# Optional: Set plot style

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# 1. Distribution of Total Crossings Over Time

sample_data = pd.DataFrame({
    'date': pd.date_range(start='2022-01-01', periods=5, freq='M'),
    'value': [100, 200, 150, 300, 250]
})

plt.figure(figsize=(14, 6))
sns.lineplot(data=sample_data, x='date', y='value', marker='o')
plt.title("📅 Sample Border Crossings")
plt.xlabel("Date")
plt.ylabel("Total Crossings")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Top 10 Ports with Highest Total Crossings
import pandas as pd;
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Border_Crossing_Entry_Data_final.csv", low_memory=False)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert date safely
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')

# Report invalid dates
invalid_count = df['date'].isnull().sum()
print(f" Invalid dates: {invalid_count}")

# Convert 'value' column to numeric with error handling
df['value'] = pd.to_numeric(df['value'], errors='coerce')
print(f"Number of NaN values after 'value' conversion: {df['value'].isnull().sum()}")

# Drop rows with missing or invalid data
df.dropna(subset=['value', 'port_name'], inplace=True)

# Group and sort to get top 10 ports
top_ports = df.groupby('port_name')['value'].sum().sort_values(ascending=False).head(10)

# Debug print for top ports
print("Top ports by value:\n", top_ports)

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=top_ports.values, y=top_ports.index, palette="viridis")
plt.title("🏙️ Top 10 Ports by Total Crossings")
plt.xlabel("Total Crossings")
plt.ylabel("Port")
plt.tight_layout()
plt.show()

# 3.Crossing Volume by Measure Type

# Report invalid dates
invalid_count = df['date'].isnull().sum()
print(f" Invalid dates: {invalid_count}")

# Convert 'value' column to numeric with error handling
df['value'] = pd.to_numeric(df['value'], errors='coerce')
print(f"Number of NaN values after 'value' conversion: {df['value'].isnull().sum()}")

# Drop rows with missing or invalid data
df.dropna(subset=['value', 'measure'], inplace=True)

# Crossing Volume by Measure Type
measure_data = df.groupby('measure')['value'].sum().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=measure_data.values, y=measure_data.index, palette="mako")
plt.title("🚗 Crossing Volume by Measure Type")
plt.xlabel("Total Crossings")
plt.ylabel("Measure")
plt.tight_layout()
plt.show()


# 4 Heatmap: Crossings by Port & Measure (Top 10 Ports)


# Report invalid dates
invalid_count = df['date'].isnull().sum()
print(f"⚠️ Invalid dates: {invalid_count}")

# Convert 'value' column to numeric with error handling
df['value'] = pd.to_numeric(df['value'], errors='coerce')
print(f"Number of NaN values after 'value' conversion: {df['value'].isnull().sum()}")

# Drop rows with missing or invalid data
df.dropna(subset=['value', 'port_name', 'measure'], inplace=True)

# Identify the top 10 ports by total crossings
top_10_ports = df['port_name'].value_counts().nlargest(10).index

# Filter the DataFrame to include only data for the top 10 ports
heatmap_data = df[df['port_name'].isin(top_10_ports)]

# Create a pivot table for the heatmap
heatmap_pivot = heatmap_data.pivot_table(index='port_name', columns='measure', values='value', aggfunc='sum', fill_value=0)

# Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("🔍 Heatmap: Total Crossings by Port & Measure")
plt.xlabel("Measure")
plt.ylabel("Port")
plt.tight_layout()
plt.show()

#  5 . Boxplot to Detect Outliers in Crossing Counts


# Report invalid dates
invalid_count = df['date'].isnull().sum()
print(f" Invalid dates: {invalid_count}")

# Convert 'value' column to numeric with error handling
df['value'] = pd.to_numeric(df['value'], errors='coerce')
print(f"Number of NaN values after 'value' conversion: {df['value'].isnull().sum()}")

# Drop rows with missing or invalid data in 'value'
df.dropna(subset=['value'], inplace=True)

# Boxplot of Crossing Values
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='value', color="salmon")
plt.title("📦 Boxplot of Crossing Values (Outlier Detection)")
plt.xlabel("Crossing Value")
plt.tight_layout()
plt.show()
































