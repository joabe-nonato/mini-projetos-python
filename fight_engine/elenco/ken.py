from settings import *

spritesheet = "ryuB.png"
gravidade =  (TELA_ALTURA * 0.032) #27px
velocidade_x = 4 #frente
velocidade_y = 0.8 #pulo
velocidade_xy = 11 #pulo diagonal
largura = (TELA_LARGURA * 0.1593)   #largura = 204px
altura = (TELA_ALTURA * 0.4625)     #altura = 444px
dimensao_padrao = [largura, altura]

bloco_golpe = (10,10, 20, 30)

# [[(DIMENSOES IMAGEM ORIGEM), (DIMENSAO IMAGEM DESTINO), [(COLISAO6),(COLISAO3),(COLISAO01)], (BLOCO GOLPE)]

colisao = (0, 0, 100,100) # esquerda, topo, largura, altura, golpe, valor
colisoes = [(0, 0, 220, 100, False, 10), (20, 100, 160, 170, False, 15), (90, 250, 75, 80, False, 20)]

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

# EM PÉ
socoforte = [
[((0,460), (60,95)), dimensao_padrao, colisoes],
[((80,460),(75,95)), (largura, 350), colisoes],
[((170,460), (110,95)), (360, 350), colisoes],
[((170,460), (110,95)), (360, 350), [(0, 0, 210, 100, False, 10), (20, 100, 160, 170, False, 15), (90, 250, 75, 80, False, 20), (175, 250, 180, 40, True, 10)]],
[((170,460), (110,95)), (360, 350), colisoes],
[((80,460),(75,95)), (largura, 350), colisoes],
[((0,460), (60,95)), dimensao_padrao, colisoes],
]

colisoes = [(0, 0, 220, 100, False, 10), (20, 100, 160, 220, False, 15), (0, 270, 90, 90, False, 20)]
chuteforte = [
[((0,1189), (60,90)), dimensao_padrao, [(120, 0, 100, 100, False, 10), (30, 100, 180, 170, False, 15), (10, 250, 130, 100, False, 20)]],
[((66,1185), (94,95)), (360, 350), [(170, 0, 90, 100, False, 10), (30, 100, 240, 170, False, 15), (160, 250, 200, 90, False, 20), (270, 300, 100, 50, True, 15)]],
[((171,1185), (121,95)), (360, 350), [(130, 0, 80, 100, False, 10), (0, 100, 220, 170, False, 15), (160, 250, 200, 90, False, 20), (170, 270, 200, 80, True, 15)]],
[((299,1200), (102,80)), (350, 330), [(140, 0, 110, 110, False, 10), (0, 100, 220, 210, False, 15), (160, 150, 200, 90, False, 20), (230, 160, 130, 120, True, 15)]],
[((412,1200), (65,81)), dimensao_padrao, [(0, 0, 220, 100, False, 10), (20, 100, 160, 220, False, 15), (0, 270, 90, 90, False, 20)]],
]

# parado = [
# [((412,1200), (65,81)), dimensao_padrao, [(0, 0, 220, 100, False, 10), (20, 100, 160, 220, False, 15), (0, 270, 90, 90, False, 20)]],
# ]

colisoes = [(0, 0, 200, 110), (0, 110, 140, 80)]
chuteagachado = [
[((1419,1217), (53,61)), (200, 200), colisoes],
[((1481,1218), (121,58)), (360, 200), [(60, 0, 300, 60), (10, 30, 165, 163)], ((0,250), (180,40))],
[((1605,1222), (64,57)), (200, 200), colisoes],
[((1675,1219), (63,60)), (200, 200), colisoes],
]


colisoes = [(630, 838, 180, 210)]
socoagachado = [
[((482,838), (65,61)), (largura, 230), colisoes],
[((552,838), (65,61)), (largura, 230), colisoes],
[((630,838), (93,61)), (300, 230), colisoes, ((100,70), (200,40))],
[((630,838), (93,61)), (300, 230), colisoes, ((100,70), (200,40))],
[((552,838), (65,61)), (largura, 230), colisoes],
[((482,838), (65,61)), (largura, 230), colisoes],
]



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
    , chuteforte
    , chuteagachado
    
]
