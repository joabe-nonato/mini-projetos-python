import PySimpleGUI as sg
import os
import platform as plf

class Pagina:
    def __init__(self) -> None:
        # self.funcao = Funcao()
        sg.theme('LightGrey 1')
        pass

    def Menu(self):
        menu = [
            [sg.Text(f'Usuário: {os.getlogin()}')],
            [sg.Text(f'Máquina: { plf.uname()[1] }')],
            [sg.Button('Organizar Por Data', size=(30, 1))],
            [sg.Button('Organizar Por Tipo', size=(30, 1))],
            [sg.Button('Copiar De Para', size=(30, 1))],
        ]

        return menu

    def OrganizaData(self):
        pass

    def OrganizaTipo(self):
        pass

    def CopiarPara(self):
        pass

    def Carregar(self):
        janela = sg.Window('Organizar Arquivos', layout= self.Menu(), finalize=True)        
        
        while True:
            event, values = janela.read(timeout=120000)    

            if event == sg.WIN_CLOSED or event == 'Cancelar': 
                break
