



class Objeto:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.largura = 0
        self.altura = 0
        self.solido = True        
        self.localx = (self.x + self.largura)
        self.localy = (self.y + self.altura)

    

    