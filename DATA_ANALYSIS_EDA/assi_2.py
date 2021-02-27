import pandas as pd
import numpy as np

df=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_2/csv_file (3).csv")
df.iloc[:,2].plot(kind='box') ## from box plot we got one outlier greater than 90
a=[df.iloc[:,2]]
b=df.describe()
c=df.var()

a1=df[df['Measure Xpercent']>90] ##taking the outlier value

##2nd question
from scipy import stats
m=1-stats.norm.cdf(50,loc=45,scale=8)
m1=stats.norm.cdf(30,loc=38,scale=6)*400
m2=stats
m2=stats.norm.cdf(44,loc=38,scale=6)-stats.norm.cdf(38,loc=38,scale=6)

q=stats.norm.interval(.95,loc=12, scale=5)
(2.2001800772997306*45, 21.79981992270027*45)

z=stats.norm.ppf(-0.125)

a1=(z*5)+12

a2=a1*45


m2=stats.norm.cdf(55,loc=50,scale=4)-stats.norm.cdf(45,loc=50,scale=4)



a


