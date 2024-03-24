import seaborn as sns
import pandas as pd

dataset = sns.load_dataset('titanic')

# # Check for null/NaN values in each column
# null_values = dataset.isnull().any()
#
# # Count the number of null/NaN values in each column
# null_count = dataset.isnull().sum()
#
# # Print which columns have null/NaN values and their counts
# print("Columns with null/NaN values:")
# print(null_values)
# print("\nCount of null/NaN values in each column:")
# print(null_count)

print(dataset)
