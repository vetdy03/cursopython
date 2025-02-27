class Arma:
    def __init__(self, tipo:str, poder:int):
        self.tipo= tipo
        self.poder = poder
        
    def get_tipo(self)->str:
        return self.tipo
    
    def get_poder(self)->int:
        return self.poder
    
    def cambiar_poder(self, valor:int):
        self.poder = valor