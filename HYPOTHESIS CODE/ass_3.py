import statsmodels.api as sm
import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/Cutlets.csv")

sm.stats.ttest_ind(df.Unit_A,df.Unit_B)


df1=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/LabTAT.csv")

import scipy.stats as sc
sc.f_oneway(df1.iloc[:,0],df1.iloc[:,1],df1.iloc[:,2],df1.iloc[:,3])

df2=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/BuyerRatio.csv")
from scipy.stats import chi2_contingency
data1=[[50,142,131,70],[550,351,480,350]]

m=chi2_contingency(data1)



df3=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/Costomer+OrderForm.csv")

m1=df3['Phillippines'].value_counts()
m2=df3['Indonesia'].value_counts()
m3=df3['Malta'].value_counts()
m4=df3['India'].value_counts()

series=[m1,m2,m3,m4]

output=pd.concat(series,axis =1)

s1=output.iloc[0,0:4]
s2=output.iloc[1,0:4]
s=[s1,s2]

new=chi2_contingency(s)


df4=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/Faltoons.csv")
n1=df4['Weekdays'].value_counts()
n2=df4['Weekend'].value_counts()
series=[n1,n2]
new=chi2_contingency(series)





