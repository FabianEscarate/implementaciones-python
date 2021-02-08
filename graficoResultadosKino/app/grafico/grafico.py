import matplotlib.pyplot as plt

class Grafica:
    def __init__(self, _data):
        self.__private_data = _data

    @classmethod
    def grafico_interactivo(self):
        plt.ion()
        plt.plot([1.6, 2.7])

        plt.title("grafico interactivo")
        plt.xlabel("index")

        ax = plt.gca()
        ax.plot([3.1, 2.2])

        plt.show(block=True)
        print("grafico")