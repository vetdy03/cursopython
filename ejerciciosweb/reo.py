class Reo:
    def __init__(self, pais, aniosDeCondena):
        self.pais = pais
        self.aniosDeCondena = aniosDeCondena
        self.gradoPeligrosidad = ""
               
    def setgradoPeligrosidad(self, aniosDeCondena):
        if aniosDeCondena >= 100:
            self.gradoPeligrosidad = "Peligrosidad Eminente"
        elif aniosDeCondena >= 50 and aniosDeCondena <= 99:
            self.gradoPeligrosidad = "Peligrosidad Alta"
        elif aniosDeCondena >= 25 and aniosDeCondena <= 49:
            self.gradoPeligrosidad = "Peligrosidad Media"
        else:
            self.gradoPeligrosidad ="Peligrosidad Baja"
            
# Creacion de instancias de reis objetos    
reo1 = Reo('Bolivia', 17)      
reo2 = Reo('Peru', 28)
reo3 = Reo('Chile', 82)
reo4 = Reo('Chino', 72)
reo5 = Reo('Alemania', 63)

# Asignar grados de peligrosidad
print("=== INFO DE REOS ===")
reos = [reo1, reo2, reo3, reo4, reo5]
for indice, reo in enumerate(reos, start=1):
    reo.setgradoPeligrosidad()
    #print(f"Reo {indice}: pais: ")
    print("soy reo de {} de la posicion {} y soy de  {}".format(reo.pais, indice, reo.gradoPeligrosidad))
    
for reo in reos:
    reo.setgradoPeligrosidad()

    
