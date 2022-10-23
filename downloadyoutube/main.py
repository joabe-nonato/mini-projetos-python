import pytubedownload as pd
import PySimpleGUI as sg

link = "https://www.youtube.com"
path = "C:\downloadyoutube"

layout = [
    [sg.Text('URL do vídeo no YouTube:')],
    [sg.Input(key="urlyt", size=(60, 2), default_text = link)],
    [sg.Text('Salvar em:')],
    [sg.Input(key="pathyt", size=(60, 2), default_text= path)],
    [sg.Button('Verificar', size=(20, 2), pad=25 ), sg.Button('Baixar', size=(20, 2), pad=30, tooltip="Caso o diretório informado não exista, ele será criado.")],
    [sg.Text('', key="mensagem")]
]

window = sg.Window("PyYouTube: Download", layout, size=(460,240))

def ValidarUrlYT(link):
    if "https://www.youtube.com/watch" in link:        
        return True
    else:
        window["mensagem"].update("URL do vídeo não é valida!")
        return False

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Verificar' and ValidarUrlYT(values["urlyt"]):
        try:
            window["mensagem"].update(" ")
            sg.popup_scrolled(pd.VerificarEstatistica(values["urlyt"]), title="Sobre o vídeo")
            window["mensagem"].update("URL do vídeo valida.")
        except:
            window["mensagem"].update("Ocorreu um erro, verifique a URL do vídeo.")
        
    elif event == 'Baixar' and ValidarUrlYT(values["urlyt"]):
        try:
            window["mensagem"].update("")
            pd.ExecutarDownalod(values["urlyt"], values["pathyt"])
            window["mensagem"].update("Vídeo baixado com sucesso.")
        except:
            window["mensagem"].update("Ocorreu um erro, verifique os valores informados.")
