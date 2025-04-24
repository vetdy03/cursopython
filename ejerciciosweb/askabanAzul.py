class Reo:
    def __init__(self, id_reo, pais, anios_condena):
        self.id_reo = id_reo
        self.pais = pais
        self.anios_condena = anios_condena
        self.grado_peligrosidad = self.calcular_grado_peligrosidad()
        self.celda_asignada = None
    
    def calcular_grado_peligrosidad(self):
        if self.anios_condena >= 100:
            return "Peligro Inminente"
        elif self.anios_condena >= 50:
            return "Peligro Alto"
        elif self.anios_condena >= 25:
            return "Peligro Medio"
        else:
            return "Peligro Bajo" 
        #demotodelete
    
    def __str__(self):
        return f"Reo {self.id_reo}: {self.pais}, {self.anios_condena} años ({self.grado_peligrosidad})"

class Celda:
    def __init__(self, codigo):
        self.codigo = codigo
        self.reos = []
        self.paises = set()
        self.grados_peligrosidad = set()
    
    def agregar_reo(self, reo):
        # Verificar restricciones
        if len(self.reos) >= 3:
            return False, "La celda está llena (máximo 3 reos)"
        
        if reo.pais in self.paises:
            return False, f"No se puede agregar: ya hay un reo de {reo.pais} en esta celda"
        
        if reo.grado_peligrosidad in self.grados_peligrosidad:
            return False, f"No se puede agregar: ya hay un reo con {reo.grado_peligrosidad} en esta celda"
        
        # Si pasa las restricciones, agregar
        self.reos.append(reo)
        self.paises.add(reo.pais)
        self.grados_peligrosidad.add(reo.grado_peligrosidad)
        reo.celda_asignada = self.codigo
        return True, "Reo agregado exitosamente"
    
    def remover_reo(self, reo):
        if reo in self.reos:
            self.reos.remove(reo)
            self.paises.remove(reo.pais)
            self.grados_peligrosidad.remove(reo.grado_peligrosidad)
            reo.celda_asignada = None
            return True
        return False
    
    def mostrar_reos(self):
        print(f"\nReos en celda {self.codigo}:")
        if not self.reos:
            print("La celda está vacía")
        for reo in self.reos:
            print(reo)
    
    def __str__(self):
        return f"Celda {self.codigo}: {len(self.reos)}/3 reos"

class SistemaAskaban:
    def __init__(self):
        self.reos = {}
        self.celdas = {}
    
    def registrar_reo(self, id_reo, pais, anios_condena):
        if id_reo in self.reos:
            print(f"Error: Ya existe un reo con ID {id_reo}")
            return False
        
        nuevo_reo = Reo(id_reo, pais, anios_condena)
        self.reos[id_reo] = nuevo_reo
        print(f"Reo {id_reo} registrado exitosamente")
        return True
    
    def crear_celda(self, codigo):
        if codigo in self.celdas:
            print(f"Error: Ya existe una celda con código {codigo}")
            return False
        
        self.celdas[codigo] = Celda(codigo)
        print(f"Celda {codigo} creada exitosamente")
        return True
    
    def asignar_reo_a_celda(self, id_reo, codigo_celda):
        if id_reo not in self.reos:
            print(f"Error: No existe reo con ID {id_reo}")
            return False
        
        if codigo_celda not in self.celdas:
            print(f"Error: No existe celda con código {codigo_celda}")
            return False
        
        reo = self.reos[id_reo]
        celda = self.celdas[codigo_celda]
        
        # Si el reo ya está en una celda, primero removerlo
        if reo.celda_asignada:
            celda_actual = self.celdas[reo.celda_asignada]
            celda_actual.remover_reo(reo)
        
        # Intentar agregar a la nueva celda
        exito, mensaje = celda.agregar_reo(reo)
        print(mensaje)
        return exito
    
    def transferir_reo(self, id_reo, codigo_celda_destino):
        return self.asignar_reo_a_celda(id_reo, codigo_celda_destino)
    
    def mostrar_reos_en_celda(self, codigo_celda):
        if codigo_celda not in self.celdas:
            print(f"Error: No existe celda con código {codigo_celda}")
            return False
        
        self.celdas[codigo_celda].mostrar_reos()
        return True
    
    def mostrar_estado_sistema(self):
        print("\n=== ESTADO DEL SISTEMA ===")
        print(f"Total reos registrados: {len(self.reos)}")
        print(f"Total celdas creadas: {len(self.celdas)}")
        
        print("\nCeldas y su ocupación:")
        for celda in self.celdas.values():
            print(celda)
        
        print("\nDetalle por celda:")
        for codigo, celda in self.celdas.items():
            celda.mostrar_reos()

# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaAskaban()
    
    # Crear algunas celdas
    sistema.crear_celda("A1")
    sistema.crear_celda("A2")
    sistema.crear_celda("B1")
    
    # Registrar algunos reos
    sistema.registrar_reo("R001", "Bolivia", 17)
    sistema.registrar_reo("R002", "Perú", 28)
    sistema.registrar_reo("R003", "Chile", 82)
    sistema.registrar_reo("R004", "China", 72)
    sistema.registrar_reo("R005", "Alemania", 63)
    sistema.registrar_reo("R006", "Francia", 105)
    sistema.registrar_reo("R007", "Italia", 30)
    sistema.registrar_reo("R008", "Brasil", 45)
    
    # Asignar reos a celdas
    sistema.asignar_reo_a_celda("R001", "A1")
    sistema.asignar_reo_a_celda("R002", "A1")
    sistema.asignar_reo_a_celda("R003", "A1")  # No debería permitir porque hay conflicto con R002 (mismo grado)
    sistema.asignar_reo_a_celda("R003", "A2")
    sistema.asignar_reo_a_celda("R004", "A2")
    sistema.asignar_reo_a_celda("R005", "A2")  # No debería permitir porque hay conflicto con R003 (mismo grado)
    
    # Mostrar estado del sistema
    sistema.mostrar_estado_sistema()
    
    # Transferir un reo
    sistema.transferir_reo("R001", "B1")
    sistema.mostrar_reos_en_celda("A1")
    sistema.mostrar_reos_en_celda("B1")
    
    # Intentar agregar reo con mismo país o mismo grado
    sistema.registrar_reo("R009", "Bolivia", 20)  # Mismo país que R001
    sistema.asignar_reo_a_celda("R009", "B1")  # No debería permitir