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
gravidade =  (TELA_ALTURA * 0.032) #27px
velocidade_x = 4 #frente
velocidade_y = 0.8 #pulo
velocidade_xy = 11 #pulo diagonal
largura = (TELA_LARGURA * 0.1593)   #largura = 204px
altura = (TELA_ALTURA * 0.4625)     #altura = 444px
dimensao_padrao = [largura, altura]

bloco_golpe = (10,10, 20, 30)

# [[(DIMENSOES IMAGEM ORIGEM), (DIMENSAO IMAGEM DESTINO), [(COLISAO6),(COLISAO3),(COLISAO01)], (BLOCO GOLPE)]

colisao = (0, 0, 100,100)
colisoes = [colisao, colisao, colisao]

parado = [
 [((0,0),  (60,100)), dimensao_padrao, colisoes]
,[((68,0), (60,100)), dimensao_padrao, colisoes]
,[((135,0),(60,100)), dimensao_padrao, colisoes]
,[((204,0),(60,100)), dimensao_padrao, colisoes]
,[((270,0),(60,100)), dimensao_padrao, colisoes]
]

frente = [
# [((2,115),  (60,100)), dimensao_padrao, colisoes],
[((71,115), (65,100)), dimensao_padrao, colisoes],
[((145,115),(65,100)), dimensao_padrao, colisoes],
[((222,115),(65,100)), dimensao_padrao, colisoes],
[((300,115),(65,100)), dimensao_padrao, colisoes],
[((357,115),(65,100)), dimensao_padrao, colisoes]
]

tras = [
[((423,109), (60,100)), dimensao_padrao, colisoes],
[((486,109), (60,100)), dimensao_padrao, colisoes],
[((550,109), (60,100)), dimensao_padrao, colisoes],
[((622,109), (60,100)), dimensao_padrao, colisoes],
[((698,109), (60,100)), dimensao_padrao, colisoes],
]

agachado = [
[((543,0), (60,100)), dimensao_padrao, [(630, 838, 180, 210)]],
[((604,0), (60,100)), dimensao_padrao, [(630, 838, 180, 210)]],
[((672,0), (63,100)), dimensao_padrao, [(630, 838, 180, 210)]],
]

pulo = [
[((60,237), (60,110)), (largura, altura + 10), colisoes],
[((131,226), (60,100)), dimensao_padrao, colisoes],
[((190,226), (60,100)), dimensao_padrao, colisoes],
[((251,233), (60,100)), dimensao_padrao, colisoes],
[((311,227), (55,100)), dimensao_padrao, colisoes],
[((368,238), (56,110)), dimensao_padrao, colisoes],
]

pulo_frente = [
[((368,238), (60,110)), (largura, altura + 10), colisoes],
[((435,254), (61,79)), dimensao_padrao, colisoes],
[((500,252), (111,48)), (altura, largura), colisoes],
[((609,234), (54,82)), dimensao_padrao, colisoes],
[((669,251), (122,45)), (altura, largura), colisoes],
[((797,252), (72,87)), dimensao_padrao, colisoes],
[((368,238), (60,110)), (largura, altura + 10), colisoes],
]

pulo_tras = [
[((368,238), (60,110)), (largura, altura + 10), colisoes],
[((435,254), (61,79)), dimensao_padrao, colisoes],
[((500,252), (111,48)), (altura, largura), colisoes],
[((609,234), (54,82)), dimensao_padrao, colisoes],
[((669,251), (122,45)), (altura, largura), colisoes],
[((797,252), (72,87)), dimensao_padrao, colisoes],
[((368,238), (60,110)), (largura, altura + 10), colisoes],
]

vitoria = [
[((358,1913), (65,100)), dimensao_padrao, colisoes],
[((424,1913), (65,100)), dimensao_padrao, colisoes],
[((497,1913), (65,100)), dimensao_padrao, colisoes],
[((570,1887), (60,125)), dimensao_padrao, colisoes],
[((631,1897), (60,115)), dimensao_padrao, colisoes],
]

socoforte = [
[((0,460), (60,95)), dimensao_padrao, colisoes],
[((80,460),(75,95)), (largura, 350), colisoes],
[((170,460), (110,95)), (360, 350), colisoes],
[((170,460), (110,95)), (360, 350), colisoes, ((0,250), (180,40))],
[((170,460), (110,95)), (360, 350), colisoes],
[((80,460),(75,95)), (largura, 350), colisoes],
[((0,460), (60,95)), dimensao_padrao, colisoes],
]

socoagachado = [
[((482,838), (65,61)), (largura, 230), colisoes],
[((552,838), (65,61)), (largura, 230), colisoes],
[((630,838), (93,61)), (300, 230), [(630, 838, 200, 200)], ((100,70), (200,40))],
[((630,838), (93,61)), (300, 230), [(630, 838, 200, 200)], ((100,70), (200,40))],
[((552,838), (65,61)), (largura, 230), [(630, 838, 93,61)]],
[((482,838), (65,61)), (largura, 230), [(630, 838, 93,61)]],
]

# socoaereo = [
# [((242,825), (68,78)), (largura, 230), colisoes],
# ]

# parado = [
# [((672,0), (63,100)), dimensao_padrao, [(672,0, 63,100)]],
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
