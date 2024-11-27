import http.client
from flask import Flask
from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}

@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"

# Endpoint para sumar dos numeros y manejar errores (TypeError, ValueError e InvalidPermissions)
@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except (TypeError, ValueError, util.InvalidPermissions) as e:
        return util.handle_error(e)

# Endpoint para restar dos numeros y manejar errores (TypeError, ValueError e InvalidPermissions)
@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except (TypeError, ValueError, util.InvalidPermissions) as e:
        return util.handle_error(e)

# Endpoint para multiplicar dos numeros y manejar errores (TypeError, ValueError e InvalidPermissions)
@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.multiply(num_1, num_2)), http.client.OK, HEADERS)
    except (TypeError, ValueError, util.InvalidPermissions) as e:
        return util.handle_error(e)

# Endpoint para dividir dos numeros y manejar errores (TypeError, ValueError e InvalidPermissions)
@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.divide(num_1, num_2)), http.client.OK, HEADERS)
    except (TypeError, ValueError, util.InvalidPermissions) as e:
        return util.handle_error(e)

# Endpoint para elevar un numero a otro y manejar errores (TypeError, ValueError e InvalidPermissions)
@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.power(num_1, num_2)), http.client.OK, HEADERS)
    except (TypeError, ValueError, util.InvalidPermissions) as e:
        return util.handle_error(e)
    
# Endpoint para calcular la raiz cuadrada de un numero y manejar errores (TypeError, ValueError e InvalidPermissions)
@api_application.route("/calc/sqrt/<op_1>", methods=["GET"])
def sqrt(op_1):
    try:
        num_1 = util.convert_to_number(op_1)
        return ("{}".format(CALCULATOR.sqrt(num_1)), http.client.OK, HEADERS)
    except (TypeError, ValueError, util.InvalidPermissions) as e:
        return util.handle_error(e)

# Endpoint para calcular el logaritmo en base 10 de un numero y manejar errores (TypeError, ValueError e InvalidPermissions)
@api_application.route("/calc/log10/<op_1>", methods=["GET"])
def log10(op_1):
    try:
        num_1 = util.convert_to_number(op_1)
        return ("{}".format(CALCULATOR.log10(num_1)), http.client.OK, HEADERS)
    except (TypeError, ValueError, util.InvalidPermissions) as e:
        return util.handle_error(e)

if __name__ == "__main__": # pragma: no cover
    api_application.run(host="localhost", port=5000, debug=True)