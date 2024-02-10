class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular(self):
        print(f"El rectangulo tiene como base {self.base} y altura {self.altura}")
              
figura = Rectangulo(15,20)
figura.calcular()

class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0  # Saldo privado

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        return self.__saldo
    

    class FiguraGeometrica:
    def calcular_area(self):
        pass  # Este método será implementado por las subclases


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

# Ejemplo de uso
triangulo = Triangulo(10, 5)
print("Área del triángulo:", triangulo.calcular_area())

cuadrado = Cuadrado(6)
print("Área del cuadrado:", cuadrado.calcular_area())