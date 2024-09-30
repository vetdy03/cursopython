class Celular:
    def __init__(self, marca, modelo, camara):
        self.marcaa = marca
        self.modeloo = modelo
        self.camaraa = marca
        
    def llamar(self):
        print(f'Estas haceindo llamda desde un: {self.modeloo}')
    
    def cortar(self):
        print(f'Estas cortando la llamda desde un: {self.modeloo}')
    
    #def cambiarMarca(self):
        #self.marcaa = marca
        
celular1 = Celular("samsung", "s23", "48mp")
celular2 = Celular("huawei", "p30", "48mp")

celular1.llamar()
#celular2.cambiarMarca()








#OBJETOS
"""
Tiene propiedades 
"" metodos 
"""