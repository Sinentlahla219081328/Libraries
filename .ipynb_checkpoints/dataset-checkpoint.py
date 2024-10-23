
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


