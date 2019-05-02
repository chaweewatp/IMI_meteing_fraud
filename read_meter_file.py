import pandas as pd



print('finish import pandas')


df_metering_all = pd.read_csv('Data/Measurement/meter_n3.csv', engine='python')
print(df_metering_all.head())
