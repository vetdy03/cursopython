# -*- coding: utf-8 -*-


def main():
    print("B I E N V E N I D O S  A  L A  P I Z Z E R I A \ntIPOS DE PIZZA \n\t1- vegetariano\n\t2-No vegetariano\n")
    tipo = input("introduce el numero correspondiente al tipo de piza que quieres: ")
    #Decisiones
    
    if tipo == 1:
        
        print("Ingredientes de la pizza vegetariana: \nt 1- Pimiento\n\t 2- Tofu\n")
        ingredientes = input("Introduce el num de ingr que deseas")
        print("Pizza vegetariana con mozarela, tomate y", end="")
        if ingredientes == "1":
            print("Pimineto")
        else:
            print("s")
    else:
        print("Ingredientes de la piza no vegetariana\n\t1- peperoni\n\t2- jamon\n\t3 -salmon ")
        ingredientes = input("Ingrese el num de ingre que desea: ")
        if ingredientes == "1":
            print("peperoni")
        else:
            print("salmon")
            
        
    
if __name__ == '__main__':
    main()   

