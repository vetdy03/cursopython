class Reo:
    def __init__(self, pais, aniosDeCondena):
        self.pais = pais
        self.aniosDeCondena = aniosDeCondena
        self.gradoPeligrosidad = self.definir_peligrosidad()

    def definir_peligrosidad(self):
        if self.aniosDeCondena >= 100:
            return "Peligro Inminente"
        elif self.aniosDeCondena >= 50:
            return "Peligro Alto"
        elif self.aniosDeCondena >= 25:
            return "Peligro Medio"
        else:
            return "Peligro Bajo"
#print(f"Reo {indice}: pais: ")
#print(f"Reo {indice}: pais: ")
"""
for indice, reo in enumerate(reos, start=1):
    reo.setgradoPeligrosidad()
    #print(f"Reo {indice}: pais: ")
    print("soy reo de {} de la posicion {} y soy de  {}".format(reo.pais, indice, reo.gradoPeligrosidad))
"""
class Celda:
    def __init__(self, codigo):
        self.codigo = codigo
        self.reos = []

    def agregar_reo(self, reo):
        if len(self.reos) >= 3:
            print(f"[{self.codigo}] Llena. No se puede agregar a {reo.pais}.")
            return False
        for r in self.reos:
            if r.pais == reo.pais:
                print(f"[{self.codigo}] Ya hay un reo de {reo.pais}.")
                return False
            if r.gradoPeligrosidad == reo.gradoPeligrosidad:
                print(f"[{self.codigo}] Ya hay un reo con peligrosidad '{reo.gradoPeligrosidad}'.")
                return False
        self.reos.append(reo)
        print(f"[{self.codigo}] Reo de {reo.pais} agregado.")
        return True

    def remover_reo(self, pais):
        for r in self.reos:
            if r.pais == pais:
                self.reos.remove(r)
                return r
        return None

    def transferir_reo(self, pais, otra_celda):
        reo = self.remover_reo(pais)
        if reo:
            if not otra_celda.agregar_reo(reo):
                self.reos.append(reo)
                print(f"Transferencia fallida. Reo de {pais} devuelto a celda {self.codigo}.")
            else:
                print(f"Reo de {pais} transferido a celda {otra_celda.codigo}.")
        else:
            print(f"No se encontro un reo de {pais} en celda {self.codigo}.")

    def mostrar_reos(self):
        print(f"--- Reos en celda {self.codigo} ---")
        if not self.reos:
            print("Celda vacia.")
        for reo in self.reos:
            print(f"{reo.pais} - {reo.aniosDeCondena} años - {reo.gradoPeligrosidad}")

# celdas registradas en la carcelde askaban
celdas = {
    "A1": Celda("A1"),
    "B2": Celda("B2"),
    "C3": Celda("C3")
}

def menu():
    while True:
        print("\n==== SISTEMA DE CONTROL DE ASKABAN ====")
        print("1. Registrar reo y asignar a celda")
        print("2. Mostrar reos en una celda")
        print("3. Transferir reo entre celdas")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            pais = input("País del reo: ")
            anios = int(input("Años de condena: "))
            celda_codigo = input("Codigo de la celda (A1, B2, C3): ").upper()
            reo = Reo(pais, anios)
            if celda_codigo in celdas:
                celdas[celda_codigo].agregar_reo(reo)
            else:
                print("Celda no encontrada.")

        elif opcion == "2":
            celda_codigo = input("Cudigo de la celda: ").upper()
            if celda_codigo in celdas:
                celdas[celda_codigo].mostrar_reos()
            else:
                print("Celda no encontrada.")

        elif opcion == "3":
            origen = input("Celda origen: ").upper()
            destino = input("Celda destino: ").upper()
            pais = input("Pais del reo a transferir: ")
            if origen in celdas and destino in celdas:
                celdas[origen].transferir_reo(pais, celdas[destino])
            else:
                print("Celdas invalidas.")

        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opcin invalida. Intenta de nuevo.")

#ejecutar el menu con lsa opiones
menu()
