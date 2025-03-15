

def pago():
    cantHorasTrabajado= float(input("Ingrese las horas trabajadas "))
    pagoPorHora= float(input("Ingrese cuanto le pagan por hora "))
    print(cantHorasTrabajado*pagoPorHora)
    
  
if __name__ =='__main__':
    pago()