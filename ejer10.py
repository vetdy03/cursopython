def ejercicio10PayasosYMuñecas():
    payasos= int(input("Ingrese el número de payasos: "))
    munecas= int(input("Ingrese el número de muñecas: "))
    taotalPesoPayasos= 112*payasos
    taotalPesoMunecas= 75*munecas
    print("la cantidad total de muñecas vendidos es: {} y payasos es: {}  \ny el peso total es: {}".
          format(taotalPesoMunecas, taotalPesoPayasos, taotalPesoMunecas+taotalPesoPayasos))

if __name__ == '__main__':
    ejercicio10PayasosYMuñecas()