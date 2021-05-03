import pandas as pd
# import psycopg2
# import config
# import holidays
# import datetime
# import numpy as np
# from numpy  import inf
# from dateutil.relativedelta import relativedelta
# from operator import attrgetter
# query manager
from setting import local_settings
from sql_scripts.manage_query import QUERYS, getQuery
# file path manager
from csv_files.manage_file import FILES, getPath
# settings
try:
    import setting
    LOCAL_SETTINGS = local_settings
except Exception as err:
    print(err)


def minable_nacional():

    # imprimir settings
    print('settings', LOCAL_SETTINGS)

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
        print('script', script)
        return script

    # Leer csv
    df_mensual = descargar_transaccional()
    mydataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [7, 7, 7]
    }

    df_minable_example = pd.DataFrame(mydataset)

    df_minable_example.to_csv(getPath(FILES.canal_20_file_1), index=False)
    return df_minable_example
