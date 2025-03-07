class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self.saldo = saldo
        self.tasa_anual = tasa_anual
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.comision_mensual = 0

    def consignar(self, cantidad):
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad):
        nuevo_saldo = self.saldo - cantidad
        if nuevo_saldo >= 0:
            self.saldo -= cantidad
            self.numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        tasa_mensual = self.tasa_anual / 12
        interes_mensual = self.saldo * tasa_mensual
        self.saldo += interes_mensual

    def extracto_mensual(self):
        self.saldo -= self.comision_mensual
        self.calcular_interes()


class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self.activa = saldo >= 10000

    def retirar(self, cantidad):
        if self.activa:
            super().retirar(cantidad)
            if self.saldo < 10000:
                self.activa = False
        else:
            print("La cuenta está inactiva, no se puede retirar dinero.")

    def consignar(self, cantidad):
        super().consignar(cantidad)
        if not self.activa and self.saldo >= 10000:
            self.activa = True

    def extracto_mensual(self):
        if self.numero_retiros > 4:
            self.comision_mensual += (self.numero_retiros - 4) * 1000
        super().extracto_mensual()
        if self.saldo < 10000:
            self.activa = False

    def imprimir(self):
        print(f"El saldo actual es: {self.saldo}")
        print(f"La comisión mensual es: {self.comision_mensual}")
        print(f"El número de transacciones es: {self.numero_consignaciones + self.numero_retiros}")
        print("")


class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self.sobregiro = 0

    def retirar(self, cantidad):
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro -= resultado
            self.saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self.sobregiro > 0:
            residuo = cantidad - self.sobregiro
            if residuo > 0:
                self.sobregiro = 0
                self.saldo += residuo
            else:
                self.sobregiro -= cantidad
        else:
            super().consignar(cantidad)

    def imprimir(self):
        print(f"El saldo actual es: {self.saldo}")
        print(f"La comisión mensual es: {self.comision_mensual}")
        print(f"El número de transacciones es: {self.numero_consignaciones + self.numero_retiros}")
        print(f"El sobregiro es: {self.sobregiro}")
        print("")


if __name__ == "__main__":
    print("Cuenta de ahorros")
    saldo_inicial_ahorros = float(input("Ingrese el saldo inicial: "))
    tasa_anual_ahorros = float(input("Ingrese la tasa de interés anual (en decimal): "))
    cuenta_ahorros = CuentaAhorros(saldo_inicial_ahorros, tasa_anual_ahorros)

    cantidad_depositar = float(input("Ingrese la cantidad a depositar: "))
    cuenta_ahorros.consignar(cantidad_depositar)

    cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
    cuenta_ahorros.retirar(cantidad_retirar)

    cuenta_ahorros.extracto_mensual()
    cuenta_ahorros.imprimir()
