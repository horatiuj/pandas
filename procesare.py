import fnmatch
import os

import pandas as pd
import sqlite3


# conn = sqlite3.connect('db.sqlite3')
# query = "SELECT * FROM shop_product "
#
# df = pd.read_sql_query(query, conn)
#
# print(df)
#
# df.to_csv('fisier.csv',sep=';')


def find( pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(name))
    return result

lista_fisiere = find('*.csv','F:\PYTHON\pandas')
print(lista_fisiere)

for i in range(len(lista_fisiere)):
    # citesc fisierele CSV si creez seturi de date pentru COMENZI TCE si pentru AWB-uri
    df_csv = pd.read_csv(lista_fisiere[i])

df_final = df_csv.copy()
df_final.to_csv('fisier2csv',sep=';')




#df_csv = pd.read_csv(resursa)