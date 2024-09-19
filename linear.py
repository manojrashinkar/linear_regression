import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('homeprices.csv')
df


#GRAPH

plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')
plt.show()


new_df = df.drop('price',axis='columns')
print(new_df)

price = df.price
print(price)

# Create linear regression object
reg = linear_model.LinearRegression()
reg.fit(new_df,price)
a = int(input("Enter the area to predict the Price"))

p = reg.predict([[a]])
print(p)

print("y=mx+c")
m = reg.coef_
b = reg.intercept_

print("coef_",m)
print("intercept_",b)