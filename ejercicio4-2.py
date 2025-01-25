class Inmueble:
    def __init__(self, id_inmobiliario, area, direccion):
        self.id_inmobiliario = id_inmobiliario
        self.area = area
        self.direccion = direccion

    def calcular_precio_venta(self):
        return self.area * self.precio_m2

    def mostrar_informacion(self):
        print(f"Identificador inmobiliario: {self.id_inmobiliario}")
        print(f"Área: {self.area} m2")
        print(f"Dirección: {self.direccion}")
        print(f"Precio de venta: ${self.calcular_precio_venta():,.0f}")


class Vivienda(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños):
        super().__init__(id_inmobiliario, area, direccion)
        self.num_habitaciones = num_habitaciones
        self.num_baños = num_baños

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de habitaciones: {self.num_habitaciones}")
        print(f"Número de baños: {self.num_baños}")


class CasaRural(Vivienda):
    precio_m2 = 1500000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, num_pisos, distancia_cabecera, altitud):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños)
        self.num_pisos = num_pisos
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de pisos: {self.num_pisos}")
        print(f"Distancia a la cabecera municipal: {self.distancia_cabecera} km")
        print(f"Altitud: {self.altitud} metros")


class CasaUrbana(Vivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, num_pisos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños)
        self.num_pisos = num_pisos

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de pisos: {self.num_pisos}")


class CasaConjuntoCerrado(CasaUrbana):
    precio_m2 = 2500000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, num_pisos, valor_administracion, areas_comunes):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños, num_pisos)
        self.valor_administracion = valor_administracion
        self.areas_comunes = areas_comunes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Valor de la administración: ${self.valor_administracion:,.0f}")
        print(f"Áreas comunes: {'Sí' if self.areas_comunes else 'No'}")


class CasaIndependiente(CasaUrbana):
    precio_m2 = 3000000


class Apartamento(Vivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, valor_administracion):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños)
        self.valor_administracion = valor_administracion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Valor de la administración: ${self.valor_administracion:,.0f}")


class Apartaestudio(Apartamento):
    precio_m2 = 1500000


class ApartamentoFamiliar(Apartamento):
    precio_m2 = 2000000


class Local(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, localizacion):
        super().__init__(id_inmobiliario, area, direccion)
        self.localizacion = localizacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Localización: {'Interno' if self.localizacion == 'interno' else 'Da a la calle'}")


class LocalComercial(Local):
    precio_m2 = 3000000

    def __init__(self, id_inmobiliario, area, direccion, localizacion, centro_comercial):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self.centro_comercial = centro_comercial

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Centro comercial: {self.centro_comercial}")


class Oficina(Local):
    precio_m2 = 3500000

    def __init__(self, id_inmobiliario, area, direccion, localizacion, es_gobierno):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self.es_gobierno = es_gobierno

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Es gobierno: {'Sí' if self.es_gobierno else 'No'}")


# Prueba del programa
def main():
    print("Apartamento Familiar:")
    apto_familiar = ApartamentoFamiliar(10367, 120, "Avenida salvador 1-3", 1, 2, 200000)
    apto_familiar.mostrar_informacion()
    print("\n")

    print("Apartaestudio:")
    aptestudio = Apartaestudio(12354, 50, "Avenida la fe 20-18", 1, 2, 0)
    aptestudio.mostrar_informacion()
    print("\n")

    print("Casa Rural:")
    casa_rural = CasaRural(305890, 200, "Finca El Encanto", 4, 3, 2, 15, 1800)
    casa_rural.mostrar_informacion()
    print("\n")

    print("Local Comercial:")
    local_comercial = LocalComercial(401234, 80, "Calle 10 #5-20", "calle", "Centro Comercial Unicentro")
    local_comercial.mostrar_informacion()
    print("\n")

    print("Oficina:")
    oficina = Oficina(501456, 100, "Carrera 7 #45-32", "interno", True)
    oficina.mostrar_informacion()


if __name__ == "__main__":
    main()

