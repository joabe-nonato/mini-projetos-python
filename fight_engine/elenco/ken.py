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
spritesheet = "ryuB.png"
gravidade = 27
velocidade_x = 4
velocidade_y = 0.8
velocidade_xy = 7
largura = (TELA_LARGURA * 0.1593)   #largura = 204
altura = (TELA_ALTURA * 0.4625)     #altura = 444
dimensao_padrao = (largura, altura)
colisao_padrao = []

# [[(DIMENSOES IMAGEM ORIGEM), (DIMENSAO IMAGEM DESTINO), [(COLISAO6),(COLISAO3),(COLISAO01)]]]

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
[((698,111), (60,100)), dimensao_padrao],
[((769,111), (65,100)), (200, 290)],
]

agachado = [
[((543,0), (60,100)), dimensao_padrao],
[((604,0), (60,100)), dimensao_padrao],
[((672,0), (63,100)), dimensao_padrao],
]

pulo = [
[((60,237), (60,100)), dimensao_padrao],
[((131,226), (60,100)), dimensao_padrao],
[((190,226), (60,100)), dimensao_padrao],
[((251,233), (60,100)), dimensao_padrao],
[((311,227), (55,100)), dimensao_padrao],
[((368,238), (56,110)), dimensao_padrao],
]

pulo_frente = [
[((368,238), (56,110)), dimensao_padrao],
[((435,254), (61,79)), dimensao_padrao],
[((500,252), (105,43)), (280,160)],
[((609,234), (54,82)), dimensao_padrao],
[((669,251), (122,45)), (280,160)],
[((797,252), (72,87)), dimensao_padrao],
[((368,238), (56,110)), dimensao_padrao],
]

pulo_tras = [
[((368,238), (56,110)), dimensao_padrao],
[((435,254), (61,79)), dimensao_padrao],
[((500,252), (105,43)), (280,160)],
[((609,234), (54,82)), dimensao_padrao],
[((669,251), (122,45)), (280,160)],
[((797,252), (72,87)), dimensao_padrao],
[((368,238), (56,110)), dimensao_padrao],
]

vitoria = [
[((358,1913), (65,100)), dimensao_padrao],
[((424,1913), (65,100)), dimensao_padrao],
[((497,1913), (65,100)), dimensao_padrao],
[((570,1887), (60,125)), dimensao_padrao],
[((631,1897), (60,115)), dimensao_padrao],
]


socoforte = [
[((0,359), (90,91)), (265, 285)],
[((91,359),(94,91)), (270, 285)],
[((0,359), (90,91)), (265, 285)],
]

personagem = [
    spritesheet
    , parado
    , frente
    , tras
    , agachado
    , pulo
    , pulo_frente
    , pulo_frente
    , vitoria
    , derrota
    , socoforte 
    , socomedia 
    , socofraco 
    , chuteforte
    , chutemedia
    , chutefraco
    , voadoraforte
    , voadoramedia
    , voadorafraco
    , especial01 
    , especial02 
    , especial03 
    , especial04 
    , especial05 
    , especial06 
    , especial07
    , especial08
    , especial09
    , especial10
]
