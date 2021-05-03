from os import path
from pathlib import Path

class QUERYS:
    peso_sku_mes_canal_10 = 'peso-sku-mes-canal 10.sql'
    pesos_material_final_canal_10 = 'pesos-material final-canal 10.sql'
    pesos_material_final_canal_20 = 'pesos-material final-canal 20.sql'
    transaccional_canal_10 = 'transaccional-canal 10.sql'
    transaccional_canal_20 = 'transaccional-canal 20.sql'


def getQuery(query):
    if query is not None:
        if query in list(vars(QUERYS).values()):
            completePath = Path(__file__).parent.absolute()
            _file = open(path.join(completePath, query), 'r')
            return _file.read()
        raise Exception('query no registrada en mantenedor QUERY')
    raise Exception('parametro Query invalido')
