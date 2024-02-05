import seaborn as sns


iris = sns.load_dataset('iris')

# Display first few rows
print(iris.head())

# Basic information about the dataset
print(iris.info())

# Statistical summary
print(iris.describe())
