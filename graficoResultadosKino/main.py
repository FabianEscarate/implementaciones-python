from app.app import App
import matplotlib.pyplot as plt
def main():
    with App() as aplicacion:
        aplicacion.run()


if __name__ == "__main__":
    # main()
    plt.ion()
    plt.plot([1.6, 2.7])

    plt.title("grafico interactivo")
    plt.xlabel("index")

    ax = plt.gca()
    ax.plot([3.1, 2.2])

    plt.show(block=True)
    print("grafico")

