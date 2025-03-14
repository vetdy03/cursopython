class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print('Estudiante estudiando')    
    
#El usuario deberia de intectuar
nombre = input(' Digame su nombre ')
edad = input("Ahora su edad ")      
grado = input('Ahora el grado ')

estudiante = Estudiante(nombre ,edad, grado)
 
print(f"""
      Datos del est: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      grado: {estudiante.grado} \n
      """) 
while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()

"""pedro = Estudiante("pedro", 23, 3)
print(pedro.grado)
"""