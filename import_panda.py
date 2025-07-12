import pandas as pd

# Load dataset
df = pd.read_csv("creditcard.csv")

# Basic info
print(df.shape)
print(df['Class'].value_counts())
print(df.head())
