import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print(df)

# Reading a CSV file
df = pd.read_csv("data.csv")

# Writing to a CSV file
df.to_csv("output.csv", index=False)

# Filtering rows where Age > 25
filtered = df[df["Age"] > 25]
print(filtered)

# Group by a column and calculate the mean salary
grouped = df.groupby("Age")["Salary"].mean()
print(grouped)


# Filling missing values with 0
df["Salary"] = df["Salary"].fillna(0)

# Dropping rows with missing values
df = df.dropna()


# Add a new column based on existing data
df["Tax"] = df["Salary"] * 0.1
print(df)


