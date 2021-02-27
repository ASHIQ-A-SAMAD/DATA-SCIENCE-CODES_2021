##asignment 4_1

import pandas as pd
import numpy as np
import seaborn as sns
df1=pd.read_csv('C:/Users/ashiq/Desktop/csv/assignment_4/delivery_time.csv')
t=df1.corr()

import statsmodels.formula.api as smf
model=smf.ols('df1.Delivery_Time~df1.Sorting_Time', data= df1).fit()

p=model.params

sns.regplot(x=df1.Sorting_Time,y=df1.Delivery_Time, data=df1)

(model.tvalues, model.pvalues)

(model.rsquared,model.rsquared_adj)



##asignment 4_2

df2=pd.read_csv('C:/Users/ashiq/Desktop/csv/assignment_4/Salary_Data.csv')
t1=df2.corr()

model1=smf.ols('df2.Salary~df2.YearsExperience', data= df2).fit()

sns.regplot(x=df2.YearsExperience,y=df2.Salary, data=df2)

p1=model1.params

(model1.tvalues, model1.pvalues)

(model1.rsquared,model1.rsquared_adj)
