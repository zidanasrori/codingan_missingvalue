import pandas as pd

# untuk membaca csv yang telah didrop pada pycham dengan read_csv
cd = pd.read_csv('shopping_data_missingvalue.csv')
# untuk memanggil file csv yang sudah ada pada pycharm
# print('shopping_data_missingvalue.csv')
# print(cd)

# # mencari data yang hilang (missing value)
column_null= cd.isnull()
# print(column_null.sum())

# # mengisi data yang kosong
# # kolom umur
rata_umur = cd['Age'].mean()
cd['Age'] = cd['Age'].fillna(rata_umur)

# # kolom annual income
income = cd['Annual Income (k$)'].mean()
cd['Annual Income (k$)'] = cd['Annual Income (k$)'].fillna(income)

# # kolom spending score
score = cd['Spending Score (1-100)'].median()
cd['Spending Score (1-100)'] = cd['Spending Score (1-100)'].fillna(score)
#
print(cd)
