from pytube import YouTube

def VerificarEstatistica(link):
    yt = YouTube(link)
    
    result = {
        "Titulo" : yt.title,
        "Views" : yt.views,
        "Tamanho" : yt.length,
        "Avaliação": yt.rating
    }

    return result

def ExecutarDownalod(link, path):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    ys.download(path)
    return result

