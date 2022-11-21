from movimentos import *
from settings import *
# indice 0 = spritesheet
# indice 1 = parado
# indice 2 = frente
# indice 3 = tras
# indice 4 = agachado
# indice 5 = pulo
# indice 6 = pulo_frente
# indice 7 = pulo_tras
spritesheet = "ryu.png"
gravidade =  (TELA_ALTURA * 0.027) #27px
velocidade_x = 4 #frente
velocidade_y = 0.8 #pulo
velocidade_xy = 11 #pulo diagonal
largura = (TELA_LARGURA * 0.1593)   #largura = 204px
altura = (TELA_ALTURA * 0.4625)     #altura = 444px
dimensao_padrao = (largura, altura)

colisao_padrao = []
bloco_golpe = (10,10, 20, 30)

# [[(DIMENSOES IMAGEM ORIGEM), (DIMENSAO IMAGEM DESTINO), (BLOCO GOLPE), [(COLISAO6),(COLISAO3),(COLISAO01)]]]

parado = [
 [((0,0),  (60,100)), dimensao_padrao]
,[((68,0), (60,100)), dimensao_padrao]
,[((135,0),(60,100)), dimensao_padrao]
,[((204,0),(60,100)), dimensao_padrao]
,[((270,0),(60,100)), dimensao_padrao]
]

frente = [
# [((2,115),  (60,100)), dimensao_padrao],
[((71,115), (65,100)), dimensao_padrao],
[((145,115),(65,100)), dimensao_padrao],
[((222,115),(65,100)), dimensao_padrao],
[((300,115),(65,100)), dimensao_padrao],
[((357,115),(65,100)), dimensao_padrao]
]

tras = [
[((423,109), (60,100)), dimensao_padrao],
[((486,109), (60,100)), dimensao_padrao],
[((550,109), (60,100)), dimensao_padrao],
[((622,109), (60,100)), dimensao_padrao],
[((698,109), (60,100)), dimensao_padrao],
]

agachado = [
[((543,0), (60,100)), dimensao_padrao],
[((604,0), (60,100)), dimensao_padrao],
[((672,0), (63,100)), dimensao_padrao],
]

pulo = [
[((60,237), (60,110)), (largura, altura + 10)],
[((131,226), (60,100)), dimensao_padrao],
[((190,226), (60,100)), dimensao_padrao],
[((251,233), (60,100)), dimensao_padrao],
[((311,227), (55,100)), dimensao_padrao],
[((368,238), (56,110)), dimensao_padrao],
]

pulo_frente = [
[((368,238), (60,110)), (largura, altura + 10)],
[((435,254), (61,79)), dimensao_padrao],
[((500,252), (111,48)), (altura, largura)],
[((609,234), (54,82)), dimensao_padrao],
[((669,251), (122,45)), (altura, largura)],
[((797,252), (72,87)), dimensao_padrao],
[((368,238), (60,110)), (largura, altura + 10)],
]

pulo_tras = [
[((368,238), (60,110)), (largura, altura + 10)],
[((435,254), (61,79)), dimensao_padrao],
[((500,252), (111,48)), (altura, largura)],
[((609,234), (54,82)), dimensao_padrao],
[((669,251), (122,45)), (altura, largura)],
[((797,252), (72,87)), dimensao_padrao],
[((368,238), (60,110)), (largura, altura + 10)],
]

vitoria = [
[((358,1913), (65,100)), dimensao_padrao],
[((424,1913), (65,100)), dimensao_padrao],
[((497,1913), (65,100)), dimensao_padrao],
[((570,1887), (60,125)), dimensao_padrao],
[((631,1897), (60,115)), dimensao_padrao],
]

socoforte = [
[((0,460), (60,95)), dimensao_padrao],
[((80,460),(75,95)), (largura, 350)],
[((170,460), (110,95)), (360, 350)],
[((170,460), (110,95)), (360, 350), ((70,70), (250,40))],
[((170,460), (110,95)), (360, 350)],
[((80,460),(75,95)), (largura, 350)],
[((0,460), (60,95)), dimensao_padrao],
]

socoagachado = [
[((482,838), (65,61)), (largura, 190)],
[((552,838), (65,61)), (largura, 190)],
[((630,838), (93,61)), (300, 190), ((90,190), (200,40))],
[((630,838), (93,61)), (300, 190),],
[((552,838), (65,61)), (largura, 190)],
[((482,838), (65,61)), (largura, 190)],
]


# parado = [
#     [((630,838), (93,61)), (300, 190), ((90,220), (215,40))],
# ]

#largura = 204px
#altura = 444px


personagem = [ 
    parado
    , frente
    , tras
    , agachado
    , pulo
    , pulo_frente
    , pulo_tras

    , socoforte 
    , socoagachado
    
    # , socomedia 
    # , socofraco 
    # , chuteforte
    # , chutemedia
    # , chutefraco
    # , voadoraforte
    # , voadoramedia
    # , voadorafraco
    # , especial01 
    # , especial02 
    # , especial03 
    # , especial04 
    # , especial05 
    # , especial06 
    # , especial07
    # , especial08
    # , especial09
    # , especial10

    # , vitoria
    # , derrota
]
