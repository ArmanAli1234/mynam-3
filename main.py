import pandas as pd
import numpy as np
import os

number=np.random.randint(23,99,size=10)
print(f"The mean of the data is : {np.mean(number)}")
print(f"The minimum element is : {np.min(number)} and maximum element is : {np.max(number)}")

df=pd.DataFrame(number,columns=['Data'])
print(df)
print(df.std())
print(df.info())
print(df.describe())