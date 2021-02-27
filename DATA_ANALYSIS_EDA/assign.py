from scipy import stats
import math
t1=stats.t.ppf(.97,1999)
t2=stats.t.ppf(.99,1999)
t3=stats.t.ppf(.98,1999)
a1=(200+(t1*(30/math.sqrt(2000))),200-(t1*(30/math.sqrt(2000))))
a2=(200+(t2*(30/math.sqrt(2000))),200-(t2*(30/math.sqrt(2000))))
a3=(200+(t3*(30/math.sqrt(2000))),200-(t3*(30/math.sqrt(2000))))

import pandas as pd
import numpy as np

df=pd.DataFrame(data={'a':[34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]})
df.mean()
df.median()
df.mode()
df.std()
df.var()

car=pd.read_csv("C:/Users/ashiq/Desktop/csv/assignment_1/Cars.csv")
 from scipy import stats
 r=car[['MPG']]
 an1= 1-(stats.norm.cdf(38,loc=car.MPG.mean(),scale=car.MPG.std()))
  an2= (stats.norm.cdf(40,loc=car.MPG.mean(),scale=car.MPG.std()))
 an3= (stats.norm.cdf(50,loc=car.MPG.mean(),scale=car.MPG.std()))-(stats.norm.cdf(20,loc=car.MPG.mean(),scale=car.MPG.std()))


r.plot(kind='hist')
r.median()

z1=stats.t.ppf(0.975,24)
z2=stats.t.ppf(0.98,24)
z3=stats.t.ppf(0.995,24)
