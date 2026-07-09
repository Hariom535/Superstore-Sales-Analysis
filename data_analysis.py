import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Data
df = pd.read_csv('train.csv')

# Step 2: Clean Data
print(df.isnull().sum())
df.dropna(inplace=True)

# Step 3: Analysis
print("Total Sales:", df['Sales'].sum())
print(df.groupby('Category')['Sales'].sum())

# Step 4: Graphs
category_sales = df.groupby('Category')['Sales'].sum()
category_sales.plot(kind='bar')
plt.title('Sales by Category')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()