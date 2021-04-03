import pandas as pd
import numpy as np

df1 = pd.read_csv('compare1.txt', names=['g', 'c', 'm'], header=0)
# print(df1)
print(f"len   : {len(df1.index)}")
print(f"na    : {df1['c'].isna().sum()}")
print(f"unique: {len(df1['c'].unique())}")
dup1 = df1.loc[df1.duplicated(subset=['c']), ['c']]
if len(dup1.index > 0):
    print("duplicate :")
    print(dup1.to_string(index=False, header=False))

df2 = pd.read_csv('compare2.txt', names=['g', 'c', 'm'], header=0)
# print(df2)
print("len   : "+str(len(df2.index)))
print("unique: "+str(len(df2['c'].unique())))
dup2 = df2.loc[df2.duplicated(subset=['c']), ['c']]
if len(dup2.index > 0):
    print("duplicates :")
    print(dup2)


df = df1.merge(df2, how='outer', on='c')
cond = df['m_x'] == df['m_y']
df['v'] = np.where(cond, True, False)
print(df)
