import unittest
from unittest.mock import patch
import pytest
from app.calc import Calculator
from app.util import InvalidPermissions

# Función simulada para validar permisos
def mocked_validation(*args, **kwargs):
    return True

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Pruebas para el metodo add
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)

    # Pruebas para el metodo substract
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)

    # Pruebas para el metodo multiply, se simula la validación de permisos
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, mock_validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(-4, self.calc.multiply(2, -2))
        self.assertEqual(4, self.calc.multiply(-2, -2))
        self.assertEqual(2.5, self.calc.multiply(2.5, 1))
        mock_validate_permissions.assert_called()

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_nan_parameter(self, mock_validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        mock_validate_permissions.assert_called()

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_invalid_permissions(self, mock_validate_permissions):
        mock_validate_permissions.side_effect = InvalidPermissions('User has no permissions')
        self.assertRaises(InvalidPermissions, self.calc.multiply, 2, 2)

    # Pruebas para el metodo divide
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(0.5, self.calc.divide(1, 2))
        self.assertEqual(0, self.calc.divide(0, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)

    def test_divide_method_fails_with_zero_division(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)

    # Pruebas para el metodo power
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(1, self.calc.power(0, 0))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
    
    def test_power_method_fails_with_zero_to_negative_power(self):
        self.assertRaises(ValueError, self.calc.power, 0, -1)

    def test_power_method_fails_with_negative_base_to_non_integer_power(self):
        self.assertRaises(ValueError, self.calc.power, -2, 0.5)

    # Pruebas para el metodo square_root
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(0, self.calc.sqrt(0))

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "4")
        self.assertRaises(TypeError, self.calc.sqrt, None)

    def test_sqrt_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.sqrt, -4)

    # Pruebas para el metodo log base 10
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertAlmostEqual(1, self.calc.log10(10), places=7)
        self.assertAlmostEqual(2, self.calc.log10(100), places=7)
        self.assertAlmostEqual(3, self.calc.log10(1000), places=7)

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "10")
        self.assertRaises(TypeError, self.calc.log10, None)

    def test_log10_method_fails_with_non_positive_number(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -1)

if __name__ == "__main__": # pragma: no cover
    unittest.main()