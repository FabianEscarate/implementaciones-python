import pandas as pd
import numpy as np
import gc

class Excel:
    __path_excel = 'KinoResultado.xlsx'
    __data_excel = None

    def __init__(self):
        dataset = pd.read_excel(self.__path_excel)
        sorteos = list(dataset.iloc[7:-3, :2].values)
        resultados = list(dataset.iloc[7:-3, 2:17].values)
        del dataset
        gc.collect()

        _newdata = list(map(lambda sorteo:
            {
                "sorteo":sorteo[1][0],
                "fecha": sorteo[1][1],
                "numeros_kino": resultados[sorteo[0]]
            }, enumerate(sorteos)))

        self.__data_excel = _newdata
        
        
