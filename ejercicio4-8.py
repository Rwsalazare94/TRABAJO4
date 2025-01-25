from abc import ABC, abstractmethod

class Equipo:
    _total_tiempo = 0

    def __init__(self, nombre, pais):
        self._nombre = nombre
        self._pais = pais
        self.lista_ciclistas = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self._pais = pais

    def agregar_ciclista(self, ciclista):
        self.lista_ciclistas.append(ciclista)

    def listar_equipo(self):
        print("Ciclistas en el equipo:")
        for ciclista in self.lista_ciclistas:
            print(f"- {ciclista.nombre}")

    def buscar_ciclista(self):
        nombre_ciclista = input('Ingrese el nombre del ciclista a buscar: ')
        for ciclista in self.lista_ciclistas:
            if ciclista.nombre == nombre_ciclista:
                print(f"Ciclista encontrado: {ciclista.nombre}")
                return
        print("Ciclista no encontrado.")

    def calcular_total_tiempo(self):
        for ciclista in self.lista_ciclistas:
            Equipo._total_tiempo += ciclista.tiempo_acumulado

    def imprimir(self):
        print(f"Nombre del equipo: {self._nombre}")
        print(f"País del equipo: {self._pais}")
        print(f"Total de tiempo: {Equipo._total_tiempo}")

class Ciclista(ABC):
    def __init__(self, identificador, nombre):
        self._identificador = identificador
        self._nombre = nombre
        self._tiempo_acumulado = 0
        self._posicion_general = None

    @abstractmethod
    def imprimir_tipo(self):
        pass

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, identificador):
        self._identificador = identificador

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tiempo_acumulado(self):
        return self._tiempo_acumulado

    @tiempo_acumulado.setter
    def tiempo_acumulado(self, tiempo_acumulado):
        self._tiempo_acumulado = tiempo_acumulado

    @property
    def posicion_general(self):
        return self._posicion_general

    @posicion_general.setter
    def posicion_general(self, posicion_general):
        self._posicion_general = posicion_general

    def imprimir(self):
        print(f"Identificador: {self._identificador}")
        print(f"Nombre: {self._nombre}")
        print(f"Tiempo acumulado: {self._tiempo_acumulado}")

class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_promedio):
        super().__init__(identificador, nombre)
        self._potencia_promedio = potencia_promedio
        self._velocidad_promedio = velocidad_promedio

    @property
    def potencia_promedio(self):
        return self._potencia_promedio

    @potencia_promedio.setter
    def potencia_promedio(self, potencia_promedio):
        self._potencia_promedio = potencia_promedio

    @property
    def velocidad_promedio(self):
        return self._velocidad_promedio

    @velocidad_promedio.setter
    def velocidad_promedio(self, velocidad_promedio):
        self._velocidad_promedio = velocidad_promedio

    def imprimir(self):
        super().imprimir()
        print(f"Potencia promedio: {self._potencia_promedio}")
        print(f"Velocidad promedio: {self._velocidad_promedio}")

    def imprimir_tipo(self):
        print("Tipo: Velocista")

class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self._aceleracion_promedio = aceleracion_promedio
        self._grado_rampa = grado_rampa

    @property
    def aceleracion_promedio(self):
        return self._aceleracion_promedio

    @aceleracion_promedio.setter
    def aceleracion_promedio(self, aceleracion_promedio):
        self._aceleracion_promedio = aceleracion_promedio

    @property
    def grado_rampa(self):
        return self._grado_rampa

    @grado_rampa.setter
    def grado_rampa(self, grado_rampa):
        self._grado_rampa = grado_rampa

    def imprimir(self):
        super().imprimir()
        print(f"Aceleración promedio: {self._aceleracion_promedio}")
        print(f"Grado de rampa: {self._grado_rampa}")

    def imprimir_tipo(self):
        print("Tipo: Escalador")

class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima):
        super().__init__(identificador, nombre)
        self._velocidad_maxima = velocidad_maxima

    @property
    def velocidad_maxima(self):
        return self._velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self, velocidad_maxima):
        self._velocidad_maxima = velocidad_maxima

    def imprimir(self):
        super().imprimir()
        print(f"Velocidad máxima: {self._velocidad_maxima}")

    def imprimir_tipo(self):
        print("Tipo: Contrarrelojista")

if __name__ == '__main__':
    equipo1 = Equipo('Sky', 'Estados Unidos')
    velocista1 = Velocista(123979, 'Geraint Thomas', 320, 25)
    escalador1 = Escalador(123980, 'Egan Bernal', 25, 10)
    contrarrelojista1 = Contrarrelojista(123981, 'Jonathan Castroviejo', 120)

    equipo1.agregar_ciclista(velocista1)
    equipo1.agregar_ciclista(escalador1)
    equipo1.agregar_ciclista(contrarrelojista1)

    velocista1.tiempo_acumulado = 365
    escalador1.tiempo_acumulado = 385
    contrarrelojista1.tiempo_acumulado = 370

    equipo1.calcular_total_tiempo()
    equipo1.imprimir()
    equipo1.listar_equipo()
