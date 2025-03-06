import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


# Load the dataset into a Pandas DataFrame
df = pd.read_csv(r'C:\Users\hetbt\Downloads\archive\diamonds.csv')
print(df.info())
print(df.describe())

df.dropna(inplace=True)

plt.figure(figsize=(10,6))
sns.histplot(df['price'],bins=50,kde=True,color='blue')
plt.title('Distribution of diamond prices')
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(x='cut',y='price', data=df)
plt.title('price vs cut quality')
plt.xlabel('cut quality')
plt.ylabel('price')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x='color',y='price',data=df)
plt.title('price vs color')
plt.xlabel('color')
plt.ylabel('price')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x='clarity',y='price',data=df)
plt.title('price vs clarity')
plt.xlabel('clarity')
plt.ylabel('price')
plt.show()

label_encoder = LabelEncoder()
df['cut'] = label_encoder.fit_transform(df['cut'])
df['color'] = label_encoder.fit_transform(df['color'])
df['clarity'] = label_encoder.fit_transform(df['clarity'])

plt.figure(figsize=(10,6))
corr=df.corr()
sns.heatmap(corr,annot=True, cmap='coolwarm', fmt=".2f",linewidths=0.5)
plt.title("correlation price")
plt.show()


plt.figure(figsize=(10,6))
sns.scatterplot(x='carat',y='price',data=df)
plt.title('carat vs price')
plt.xlabel('carat')
plt.ylabel('price')
plt.show()

print(df[['carat', 'price']].dtypes)
