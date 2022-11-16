# indice 0 = spritesheet
# indice 1 = parado
# indice 2 = frente
# indice 3 = tras
# indice 4 = agachado
# indice 5 = pulo
# indice 6 = pulo_frente
# indice 7 = pulo_tras

dimensao_padrao = (0,0)

# [[(IMAGEM), (DIMENSAO)], [(COLISAO15),(COLISAO10),(COLISAO05)]]

parado = [
((0,0), (60,100))
,((68,0), (60,100))
,((135,0), (60,100))
,((204,0), (60,100))
,((270,0), (60,100))
]

frente = [
    ((2,115), (63,100))
, ((69,115), (70,100))
, ((145,115), (70,100))
, ((222,115), (65,100))
, ((300,115), (65,100))
, ((364,115), (55,100)) 
]

tras = [((423,115), (65,100)), ((486,115), (65,100)), ((550,115), (65,100)), ((622,115), (65,100)), ((698,115), (65,100)), ((769,115), (65,100))]

agachado = [((543,0), (60,100)), ((604,0), (60,100)), ((672,0), (63,100))]

pulo = [((1,260), (60,100)), ((60,237), (60,100)), ((131,226), (60,100)), ((190,226), (60,100)), ((251,233), (60,100)), ((311,227), (55,100)), ((368,238), (56,110))]

pulo_diagonal = [((368,238), (56,110)), ((435,254), (61,79)), ((500,252), (105,43)), ((609,234), (54,82)), ((669,251), (122,45)), ((797,252), (72,87)), ((368,238), (56,110))]

vitoria = [((358,1913), (65,100)), ((424,1913), (65,100)), ((497,1913), (65,100)), ((570,1887), (60,125)), ((631,1897), (60,115))]

derrota = []

socoforte = []
socomedia = []
socofraco = []

chuteforte = []
chutemedia = []
chutefraco = []

voadoraforte = []
voadoramedia = []
voadorafraco = []

especial01 = []
especial02 = []
especial03 = []
especial04 = []
especial05 = []
especial06 = []
especial07 = []
especial08 = []
especial09 = []
especial10 = []


ryu=["ryu.png"
    , parado
    , frente
    , tras
    , agachado
    , pulo
    , pulo_diagonal
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
