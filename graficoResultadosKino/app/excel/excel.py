import pandas as pd
import numpy as np
import gc

class Excel:
    __path_excel = 'KinoResultadoTest.xlsx'
    __data_excel = None

    def __init__(self):
        dataset = pd.read_excel(self.__path_excel)
        sorteos = dataset.iloc[7:-3, :2].reset_index(drop=True)
        sorteos.columns = ['sorteo','fecha']
        sorteos.set_index('sorteo')
        resultados = dataset.iloc[7:-3, 2:17].reset_index(drop=True)
        resultados.columns = np.arange(1, len(resultados.columns) + 1, dtype=object)
        del dataset
        gc.collect()

        _newdata = list(map(lambda sorteo:
            {
                "sorteo":sorteo[1][0],
                "fecha": sorteo[1][1],
                "numeros_kino": resultados[sorteo[0]]
            }, enumerate(sorteos)))

        self.__data_excel = _newdata
        
        
