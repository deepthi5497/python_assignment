# import pandas as pd
# Data = [1, 3, 4, 5, 6, 2, 9]
# s = pd.Series(Data)
# print(s)
# Data1 = [1, 3, 4, 5, 6, 2, 9]
# s1 = pd.DataFrame(Data1)
# print(s1)
# Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# si = pd.Series(Data, Index)
# print(si)
# Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# si1 = pd.Series(Data, Index)
# print(si1)
# print(pd.Series([1., 2., 3.], index=['a', 'b', 'c']))
# print(pd.Series([2.,3.,4.]))
import numpy as np
# h = [[1,2],[3,4]]
# df_h = pd.DataFrame(h)
# print('Data Frame:',df_h)
#
# dic = {'Name': ["John", "Smith"], 'Age': [30, 40]}
# print(pd.DataFrame(data=dic))

# dates_d = pd.date_range('20300101', periods=6, freq='D')
# print('Day:', dates_d)
# dates_d1 = pd.date_range('20300101', periods=6, freq='Y')
# print('Day:', dates_d1)
# dates_d2 = pd.date_range('20300101', periods=6, freq='M')
# print('Day:', dates_d1)
# dates_d1 = pd.date_range('20300101', '20300104')
# print
# random = np.random.randn(6,4)
# print(random)
# dates_m = pd.date_range('20300101', periods=6, freq='M')
# df = pd.DataFrame(random,
#                   index=dates_m,
#                   columns=list('ABCD'))
# print(df.head(3))
# print(df.tail(3))
# print(df.describe())
# print(df['A'])
# print(df[['A', 'B']])
# print(df.loc[:,['A','B']])
# Import pandas
import pandas as pd
print(pd.read_csv("sample.csv"))
