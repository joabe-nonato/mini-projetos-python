from pagina import *

import os
import shutil



class Organizador:
    def __init__(self) -> None:
        self.pagina = Pagina()
        self.diretorio = r'D:\teste'
        self.arquivos = os.listdir(self.diretorio)
        self.acao = 1
        pass

    def run(self):
        # self.pagina.Carregar()


        for arquivo in self.arquivos:
            if '.' in arquivo:
                extensao = arquivo.split('.')[1].lower()
                novodiretorio = f'{self.diretorio}\{extensao}'
                origem = f'{self.diretorio}\{arquivo}'
                destino = f'{self.diretorio}\{extensao}\{arquivo}'

                if os.path.exists(novodiretorio) == False:
                    os.mkdir(novodiretorio)                

                if self.acao == 1:
                    # copiar
                    shutil.copy(origem, destino)
                
                elif self.acao == 2:
                    #mover
                    if os.path.exists(destino):
                        os.remove(destino)
                    os.rename(origem, destino)
                
        


if __name__ == "__main__":
    prog = Organizador()
    prog.run()
