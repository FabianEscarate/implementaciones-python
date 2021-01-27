from app.app import App

def main():
    with App() as aplicacion:
        aplicacion.run()


if __name__ == "__main__":
    main()

