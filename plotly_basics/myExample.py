import pandas as pd
df=pd.read_csv('salaries.csv')
print(df)
print(df.Salary.max())
print(df.Salary.min())
print(df.Salary.mean())

# select the items that with an age that is larger than 30
ser_of_bool=df.Age>30
print(df[ser_of_bool])

# grab unique values in a column
age_unique=df.Age.unique()
print(age_unique)

# calculate the number of unique values in a column
n_age_unique=df.Age.nunique()
print(n_age_unique)

# grab all the column name of a dataframe
column_name=df.columns
print(column_name)

# report back the information about the dataframe
info=df.info()
print(info)

#report back the statistical summary of the dataframe
dataSum=df.describe()
print(dataSum)

# create dataFrame with numpy

import numpy as np

mat=np.arange(0,50).reshape(5,10)
print(mat)
df=pd.DataFrame(data=mat)
print(df)

new_mat=np.arange(0,10).reshape(5,2)
df=pd.DataFrame(data=new_mat,columns=['A','B'])
print(df)