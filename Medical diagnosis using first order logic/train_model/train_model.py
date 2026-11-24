import pandas as pd

# Load diagnosis dataset
df = pd.read_csv("datasets/heart.csv")

print("="*50)
print("FIRST 5 RECORDS")
print("="*50)

print(df.head())

print("\n" + "="*50)
print("COLUMN NAMES")
print("="*50)

print(df.columns.tolist())

print("\n" + "="*50)
print("DATASET SHAPE")
print("="*50)

print(df.shape)

print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)

print(df.isnull().sum())