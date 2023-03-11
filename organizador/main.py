from pagina import *



class Organizador:
    def __init__(self) -> None:
        self.pagina = Pagina()
        pass

    def run(self):
        self.pagina.Carregar()
        


if __name__ == "__main__":
    prog = Organizador()
    prog.run()
