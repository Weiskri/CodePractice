import pandas as pd
import numpy as np

# Load CSV Data
df_starting = pd.read_csv('data/StartingData.csv', index_col='User Id')
df_jan = pd.read_csv('data/Jan.csv')
df_feb = pd.read_csv('data/Feb.csv')
df_mar = pd.read_csv('data/Mar.csv')

# Sort through the Lists and Find Highest Deposit Each Month

jan_sorted = df_jan.sort_values(['Amount'])
feb_sorted = df_feb.sort_values(['Amount'])
mar_sorted = df_mar.sort_values(['Amount'])

print('January highest deposit details:')
print(jan_sorted.tail(1))
print('*********')

print('February highest deposit details:')
print(feb_sorted.tail(1))
print('*********')

print('March highest deposit details:')
print(mar_sorted.tail(1))
print('*********')

# Sort through the Lists and Find the User with the Most Transactions Each Month

jan_duplicates = df_jan[df_jan.duplicated(['User Id'], keep=False)]
counted = var = jan_duplicates.groupby('User Id').count()
most_transactions_jan = counted.sort_values('Amount').tail(3)
jan_transactions = most_transactions_jan[most_transactions_jan.duplicated(['Amount'], keep=False)]

print('Most transactions in January with Amount of Transactions')
print(jan_transactions[['Amount']])
print('*********')

feb_duplicates = df_feb[df_feb.duplicated(['User Id'], keep=False)]
counted = var = feb_duplicates.groupby('User Id').count()
most_transactions_feb = counted.sort_values('Amount').tail(3)
feb_transactions = most_transactions_feb[most_transactions_feb.duplicated(['Amount'], keep=False)]

print('Most transactions in February with Amount of Transactions')
print(feb_transactions[['Amount']])
print('*********')

mar_duplicates = df_mar[df_mar.duplicated(['User Id'], keep=False)]
counted = var = mar_duplicates.groupby('User Id').count()
most_transactions_mar = counted.sort_values('Amount').tail(3)
mar_transactions = most_transactions_mar[most_transactions_mar.duplicated(['Amount'], keep=False)]

print('Most transactions in March with Amount of Transactions')
print(mar_transactions[['Amount']])
print('*********')

# Determine who owes a penalty based on type of account and activity

