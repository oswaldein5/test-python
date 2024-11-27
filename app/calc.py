from app import util
from math import log10, sqrt

class Calculator:
    # Método para sumar dos numeros
    def add(self, x, y):
        util.validate_permissions("add", "user1")
        util.validate_operands(x, y)
        return x + y

    # Método para restar dos numeros
    def substract(self, x, y):
        util.validate_permissions("substract", "user1")
        util.validate_operands(x, y)
        return x - y

    # Método para multiplicar dos numeros
    def multiply(self, x, y):
        util.validate_permissions("multiply", "user1")
        util.validate_operands(x, y)
        return x * y

    # Método para dividir dos numeros
    def divide(self, x, y):
        util.validate_permissions("divide", "user1")
        util.validate_operands(x, y)
        util.validate_division(y)
        return x / y

    # Método para elevar un numero a otro
    def power(self, x, y):
        util.validate_permissions("power", "user1")
        util.validate_operands(x, y)
        util.validate_power(x, y)
        return x ** y

    # Método para calcular la raiz cuadrada de un numero
    def sqrt(self, x):
        util.validate_permissions("sqrt", "user1")
        util.validate_operands(x)
        util.validate_negative(x)
        return sqrt(x)

    # Método para calcular el logaritmo en base 10 de un numero
    def log10(self, x):
        util.validate_permissions("log10", "user1")
        util.validate_operands(x)
        util.validate_log(x)
        return log10(x)

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    try:
        result = calc.add(2, 2)
        print("2 + 2 = ", result)
        result = calc.substract(2, 2)
        print("2 - 2 = ", result)
        result = calc.multiply(2, 5)
        print("2 * 5 = ", result)
        result = calc.divide(10, 2)
        print("10 / 2 =", result)
        result = calc.power(6, 2)
        print("6 ^ 2", result)
        result = calc.sqrt(64)
        print("sqrt(64) = ", result)
        result = calc.log10(1000)
        print("log10(1000) = ", result)
        result = calc.divide(2, 0)
    except (TypeError, ValueError, util.InvalidPermissions) as e:
        print(e)
