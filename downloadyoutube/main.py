import pytubedownload as pd
import PySimpleGUI as sg


link = "https://www.youtube.com"
path = "C:\downloadyoutube"

layout = [
    [sg.Text('URL do vídeo no YouTube:')],
    [sg.Input(key="urlyt", size=(49, 2), default_text = link)],
    [sg.Text('Salvar em:')],
    [sg.Input(key="pathyt", size=(49, 2), default_text= path)],
    [sg.Button('Verificar', size=(20, 2)), sg.Button('Baixar', size=(20, 2))],
    [sg.Text('', key="mensagem" )]
]

window = sg.Window("PyYouTube: Ladino", layout)

def ValidarUrlYT(link):
    if "https://www.youtube.com/watch" in link:        
        return True
    else:
        window["mensagem"].update("URL do vídeo não é valida!")
        return False

while True:
    event, values = window.read()
    
    link = values["urlyt"]
    path = values["pathyt"]

    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Verificar' and ValidarUrlYT(link):
        try:
            window["mensagem"].update(" ")
            pd.VerificarEstatistica(link)
            window["mensagem"].update("URL do vídeo valida.")
        except:
            window["mensagem"].update("Ocorreu um erro, verifique a URL do vídeo.")
        
    elif event == 'Baixar' and ValidarUrlYT(link):
        try:
            window["mensagem"].update(" ")
            pd.ExecutarDownalod(link, path)
            window["mensagem"].update("Vídeo baixado com sucesso.")
        except:
            window["mensagem"].update("Ocorreu um erro, verifique os valores informados.")

        

