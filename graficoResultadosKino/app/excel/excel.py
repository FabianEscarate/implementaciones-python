import pandas as pd

class Excel:
    __path_excel = 'KinoResultado.xlsx'
    __data_excel = None

    def __init__(self):
        with pd.read_excel(self.__path_excel) as dataset:
            resultados = dataset.iloc[8:, 2:17]
    
