import http.client

# Clase para manejar excepciones de permisos
class InvalidPermissions(Exception):
    pass

# Función para convertir un operador a número
def convert_to_number(operand):
    try:
        if "." in operand:
            return float(operand)
        else:
            return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")

# Función simulada para validar permisos
def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")
    
    calculator_methods = ["add", "substract", "multiply", "divide", "power", "sqrt", "log10"]
    
    # Función para verificar que la operación esté en los métodos de la calculadora y que el usuario sea user1
    if operation not in calculator_methods or user != "user1":
        raise InvalidPermissions('User has no permissions')
    return True

# Función para validar operandos
def validate_operands(*operands):
    for operand in operands:
        if not isinstance(operand, (int, float)):
            raise TypeError("All operands must be numbers")
    return True

# Función para validar que la división no sea por cero
def validate_division(y):
    if y == 0:
        raise TypeError("Division by zero is not possible")
    return True

# Función para validar que el número no sea negativo
def validate_negative(*operands):
    for operand in operands:
        if operand < 0:
            raise TypeError("Negative numbers are not allowed")
    return True

# Función para validación de potencias
def validate_power(x, y):
    if x == 0 and y < 0:
        raise ValueError("Cannot raise zero to a negative power")
    if x < 0 and not isinstance(y, int):
        raise ValueError("Cannot raise a negative base to a non-integer power")
    return True

# Función para validación de logaritmos
def validate_log(x):
    if x <= 0:
        raise TypeError("Logarithm of non-positive numbers is not possible")
    return True

# Función para manejar errores en la API
def handle_error(e):
    return (str(e), http.client.BAD_REQUEST, {"Content-Type": "text/plain"})