import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a pandas DataFrame
file_path = 'Library_Services.csv'  # Replace with your file path if needed
data = pd.read_csv(file_path)

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Display basic information about the dataset
print("Library Services Data Here!\n")
print(df.head(20))  # Display the first 20 rows

# Display the number of rows and columns
print(f"\nNumber of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

# Display the column names and their data types
print("\nColumn Names and Data Types:\n")
print(df.dtypes)

# Display summary statistics for numerical columns
print("\nSummary Statistics for Numerical Columns:\n")
print(df.describe())


# Descriptive Statistics for Categorical Columns
print("\nValue Counts for Categorical Columns:\n")
categorical_columns = ['Branch', 'City', 'Wi-Fi']  # Add relevant categorical columns here
for col in categorical_columns:
    print(f"\nValue counts for {col}:\n")
    print(df[col].value_counts())

# Step 2: Data Visualization
# Set seaborn style for plots
sns.set(style="whitegrid")

# Histogram for numerical columns (e.g., 'Inventory', 'Square Feet')
plt.figure(figsize=(10, 6))
sns.histplot(df['Inventory'], kde=True, color='blue')
plt.title('Distribution of Inventory')
plt.xlabel('Inventory')
plt.ylabel('Frequency')
plt.show()

# Histogram for 'Square Feet'
plt.figure(figsize=(10, 6))
sns.histplot(df['Square Feet'], kde=True, color='green')
plt.title('Distribution of Square Feet')
plt.xlabel('Square Feet')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to show relationships between 'Square Feet' and 'Inventory'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Square Feet', y='Inventory', data=df)
plt.title('Relationship between Square Feet and Inventory')
plt.xlabel('Square Feet')
plt.ylabel('Inventory')
plt.show()

# Display 7 columns and 5 rows before identifying missing values
print("Displaying 7 columns and 5 rows of the dataset:")
print(df.iloc[:5, :7])

# Identify missing values
missing_data = df.isnull().sum()
print("Missing data in each column:")
print(missing_data)

# Handle missing values in the 'Branch' column
# Option 1: Fill missing 'Branch' values with 'Unknown'
df['Branch'].fillna('Unknown', inplace=True)

# Step 1: Data Manipulation



# Alternatively, if you want to display specific columns before filtering:
print("\nDisplaying relevant columns (Square Feet, City, Branch) before filtering:\n")
print(df[['Square Feet', 'City', 'Branch']].head())

# Filter data for libraries that have more than 10000 square feet and are in Cape Town
filtered_data = df[(df['Square Feet'] > 10000) & (df['City'] == 'Rockville ')]
print("\nFiltered Data for libraries with more than 10000 square feet in Rockville :\n")
print(filtered_data)

# Grouping by 'City' and aggregating on the 'Inventory' column (total and average inventory per city)
grouped_data = df.groupby('City').agg(
    total_inventory=pd.NamedAgg(column='Inventory', aggfunc='sum'),
    average_inventory=pd.NamedAgg(column='Inventory', aggfunc='mean')
).reset_index()

print("\nTotal and Average Inventory by City:\n")
print(grouped_data)

# Add a new column 'Inventory to Space Ratio' to analyze the ratio of Inventory to Square Feet
df['Inventory to Space Ratio'] = df['Inventory'] / df['Square Feet']
print("\nData with new 'Inventory to Space Ratio' column:\n")
print(df[['Branch', 'City', 'Inventory', 'Square Feet', 'Inventory to Space Ratio']].head())