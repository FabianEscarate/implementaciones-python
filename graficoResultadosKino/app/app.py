from app.excel.excel import Excel
from app.grafico.grafico import Grafica

class App:
    def __init__(self):
        # configuracion / atributos que quieras agregar a la app
        # como por ejemplo un logger
        pass
    
    def __enter__(self):
        return self    

    def __exit__(self, type, value, traceback):
        pass

    def run(self):
        # codigo del aplicativo
        # excel_obj = Excel()
        # generacion de grafico
        grafico_obj = Grafica([1,2,3,4])
        grafico_obj.grafico_interactivo()
        