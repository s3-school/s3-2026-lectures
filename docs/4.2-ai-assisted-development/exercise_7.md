# Exercise 7: Use Context7
Consider the following script.
```python 
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('customer_data.csv')


customer_subset = df.ix[0:100, ['age', 'income', 'purchase']]


mean_age = pd.np.mean(df['age'])
std_income = pd.np.std(df['income'])


new_row = pd.DataFrame({'age': [25], 'income': [50000], 'purchase': [1]})
df = df.append(new_row, ignore_index=True)


df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)


X = df[['age', 'income']]
y = df['purchase']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)

print(f"Model accuracy: {model.score(X_test, y_test)}")
```

### Question 1:
Use AI to generate `sample_data.csv` that matches the schema of the dataset used in the code above.

### Question 2:
Use AI and context7 to update the code.