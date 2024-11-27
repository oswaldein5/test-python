import http.client
import os
import unittest
from urllib.request import urlopen
import urllib.error
import pytest

BASE_URL = os.environ.get("BASE_URL", "http://localhost:5000")
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    
    # Prueba para validar que la URL no sea nula y tenga al menos 8 caracteres
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # Prueba para validar la suma de dos números
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "4")

    # Prueba para validar la resta de dos números
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "2")

    # Prueba para validar la multiplicación de dos números
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "12")

    # Prueba para validar la división de dos números
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "5.0")

    # Prueba para validar la división por cero
    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    # Prueba para validar la potencia de dos números
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "8")
    
    # Prueba para validar la potencia de un número negativo
    def test_api_power_negative_base(self):
        url = f"{BASE_URL}/calc/power/-2/3.5"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    # Prueba para validar la raiz cuadrada de un número
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "4.0")

    # Prueba para validar la raiz cuadrada de un número negativo
    def test_api_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-16"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    # Prueba para validar el logaritmo base 10 de un número
    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertAlmostEqual(float(response.read().decode()), 1, places=7)

    # Prueba para validar el logaritmo de un número cero o negativo
    def test_api_log10_non_positive(self):
        # log(0) no es valido
        url = f"{BASE_URL}/calc/log10/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")
        # log(-10) no es valido
        url = f"{BASE_URL}/calc/log10/-10"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

if __name__ == "__main__": # pragma: no cover
    unittest.main()