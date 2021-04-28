# import pandas as pd
# import psycopg2
# import config
# import holidays
# import datetime
# import numpy as np
# from numpy  import inf
# from dateutil.relativedelta import relativedelta
# from operator import attrgetter
from sql_scripts.manage_query import QUERYS, getQuery

def minable_nacional():
    # Connect to the PostgreSQL database
    # try:
    #     conn = psycopg2.connect(host='127.0.0.1', database='test', user='test_user', port=5432, password='test_password')
    #     print('conexión exitosa')

    #     def create_pandas_table(sql_query, database=conn):
    #         table = pd.read_sql_query(sql_query, database)
    #         return table

    # except:
    #     print('no se pudo conectar')

    # A function that takes in a PostgreSQL query and outputs a pandas database

    def descargar_transaccional():
        print('conectado a servidor')
        
        script = getQuery(QUERYS.transaccional_canal_10)
      
        return script

    #Leer csv
    df_mensual = descargar_transaccional()
    print('script', df_mensual)
    # df_minable.to_csv(r'../df/resultado.csv',index=False)
    # return df_minable