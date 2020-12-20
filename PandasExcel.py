
import pandas as pd
myCsv = pd.read_csv('C:\\DS\\EMI.csv')
print(myCsv.describe())
print(myCsv.info())
print(myCsv.head(5))
print(myCsv.tail(3))
print('maximum interest paid: Rs ',myCsv['Interest'].max())
print('minimum interest paid: Rs ',myCsv['Interest'].min())
print('interest paid data for more than Rs 40000',myCsv[myCsv['Interest']>40000])