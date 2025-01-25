from abc import ABC, abstractmethod

# Clase raíz Animal
class Animal(ABC):
    def __init__(self, sonido: str, alimentos: str, habitat: str, nombre_cientifico: str):
        self.sonido = sonido
        self.alimentos = alimentos
        self.habitat = habitat
        self.nombre_cientifico = nombre_cientifico

    @abstractmethod
    def getNombreCientífico(self) -> str:
        pass

    @abstractmethod
    def getSonido(self) -> str:
        pass

    @abstractmethod
    def getAlimentos(self) -> str:
        pass

    @abstractmethod
    def getHábitat(self) -> str:
        pass

# Subclase Cánido
class Canido(Animal):
    def __init__(self, sonido: str, alimentos: str, habitat: str, nombre_cientifico: str):
        super().__init__(sonido, alimentos, habitat, nombre_cientifico)

    def getNombreCientífico(self) -> str:
        return self.nombre_cientifico

    def getSonido(self) -> str:
        return self.sonido

    def getAlimentos(self) -> str:
        return self.alimentos

    def getHábitat(self) -> str:
        return self.habitat

# Subclase Felino
class Felino(Animal):
    def __init__(self, sonido: str, alimentos: str, habitat: str, nombre_cientifico: str):
        super().__init__(sonido, alimentos, habitat, nombre_cientifico)

    def getNombreCientífico(self) -> str:
        return self.nombre_cientifico

    def getSonido(self) -> str:
        return self.sonido

    def getAlimentos(self) -> str:
        return self.alimentos

    def getHábitat(self) -> str:
        return self.habitat

# Subclase Perro (Cánido)
class Perro(Canido):
    def __init__(self):
        super().__init__("Ladrido", "Carnívoro", "Doméstico", "Canis lupus familiaris")

# Subclase Lobo (Cánido)
class Lobo(Canido):
    def __init__(self):
        super().__init__("Aullido", "Carnívoro", "Bosque", "Canis lupus")

# Subclase León (Felino)
class Leon(Felino):
    def __init__(self):
        super().__init__("Rugido", "Carnívoro", "Pradera", "Panthera leo")

# Subclase Gato (Felino)
class Gato(Felino):
    def __init__(self):
        super().__init__("Maullido", "Ratones", "Doméstico", "Felis silvestris catus")

# Clase de prueba con el método main
if __name__ == "__main__":
    animales = [Gato(), Perro(), Lobo(), Leon()]
    for animal in animales:
        print(f"Nombre científico: {animal.getNombreCientífico()}")
        print(f"Sonido: {animal.getSonido()}")
        print(f"Alimentos: {animal.getAlimentos()}")
        print(f"Hábitat: {animal.getHábitat()}")
        print("-" * 40)
