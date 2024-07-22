import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
df = pd.read_csv(url, header=None, names=column_names)

# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Display the data types
print(df.dtypes)

# Basic statistics
print(df.describe())

# Plot histograms of each feature
df.hist(bins=20, figsize=(12, 8), edgecolor='black')
plt.suptitle('Feature Distributions')
plt.show()

# Scatter plot matrix
scatter_matrix(df, figsize=(12, 8), diagonal='kde')
plt.suptitle('Scatter Matrix')
plt.show()

# Box plots for each feature grouped by species
df.boxplot(by='Species', figsize=(12, 8))
plt.suptitle('Box Plots by Species')
plt.show()

# Calculate mean values of each feature for each species
mean_values = df.groupby('Species').mean()

# Plot mean values
mean_values.plot(kind='bar', figsize=(12, 6))
plt.title('Mean Values of Features by Species')
plt.ylabel('Mean Value')
plt.show()
