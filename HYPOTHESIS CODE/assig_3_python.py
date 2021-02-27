import statsmodels.api as sm
import numpy as np
import pandas as pd



##qn_1_f&b_MANAGER
df=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/Cutlets.csv")
M=sm.stats.ttest_ind(df.Unit_A,df.Unit_B)

##QN_2_HOSPITAL
import scipy.stats as sc
df1=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/LabTAT.csv")
sc.f_oneway(df1.iloc[:,0],df1.iloc[:,1],df1.iloc[:,2],df1.iloc[:,3])

##qn_2_1(values given in PPT is taken, which is different with csv file value)

from scipy.stats import chi2_contingency
data1=[[50,142,131,70],[550,351,480,350]]

m=chi2_contingency(data1)

##qn_3_TeleCall 

df3=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/Costomer+OrderForm.csv")
m1=df3['Phillippines'].value_counts()
m2=df3['Indonesia'].value_counts()
m3=df3['Malta'].value_counts()
m4=df3['India'].value_counts()
series=[m1,m2,m3,m4]
output=pd.concat(series,axis =1)

from scipy.stats import chi2_contingency
s1=output.iloc[0,0:4]
s2=output.iloc[1,0:4]
s=[s1,s2]
new=chi2_contingency(s)











## qn_4_fantaloons
import numpy as np
import pandas as pd

df4=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_3/Faltoons.csv")

from  sklearn.preprocessing import LabelEncoder
LabelEncoder= LabelEncoder()
d1=LabelEncoder.fit_transform(df4['Weekdays'])
d2=LabelEncoder.fit_transform(df4['Weekend'])

import statsmodels.api as sm
sm.stats.ttest_ind(d1,d2)
