import unittest
import pytest
import http.client
from app import util

@pytest.mark.unit
class TestUtil(unittest.TestCase):
    
    # Pruebas para convert_to_number
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

    # Pruebas para validate_permissions
    def test_validate_permissions_correct(self):
        self.assertTrue(util.validate_permissions("multiply", "user1"))

    def test_validate_permissions_invalid(self):
        self.assertRaises(util.InvalidPermissions, util.validate_permissions, "factorial", "user1")
        self.assertRaises(util.InvalidPermissions, util.validate_permissions, "factorial", "user2")
        self.assertRaises(util.InvalidPermissions, util.validate_permissions, "add", "user2")

    # Pruebas para validate_operands
    def test_validate_operands_correct(self):
        self.assertTrue(util.validate_operands(1, 2.0, -3, 4.5))

    def test_validate_operands_invalid(self):
        self.assertRaises(TypeError, util.validate_operands, 1, "2", 3)
        self.assertRaises(TypeError, util.validate_operands, "1", 2, 3)
        self.assertRaises(TypeError, util.validate_operands, 1, 2, None)

    # Pruebas para validate_division
    def test_validate_division_correct(self):
        self.assertTrue(util.validate_division(1))

    def test_validate_division_by_zero(self):
        self.assertRaises(TypeError, util.validate_division, 0)

    # Pruebas para validate_negative
    def test_validate_negative_correct(self):
        self.assertTrue(util.validate_negative(1, 2.0, 0))

    def test_validate_negative_invalid(self):
        self.assertRaises(TypeError, util.validate_negative, -1)
        self.assertRaises(TypeError, util.validate_negative, 1, -2.0)

    # Pruebas para validate_power
    def test_validate_power_correct(self):
        self.assertTrue(util.validate_power(2, 3))
        self.assertTrue(util.validate_power(2, -3))
        self.assertTrue(util.validate_power(-2, 3))

    def test_validate_power_invalid(self):
        self.assertRaises(ValueError, util.validate_power, 0, -1)
        self.assertRaises(ValueError, util.validate_power, -2, 0.5)

    # Pruebas para validate_log
    def test_validate_log_correct(self):
        self.assertTrue(util.validate_log(1))
        self.assertTrue(util.validate_log(0.1))

    def test_validate_log_invalid(self):
        self.assertRaises(TypeError, util.validate_log, 0)
        self.assertRaises(TypeError, util.validate_log, -1)
    
    # Pruebas para handle_error
    def test_handle_error(self):
        error_message = "This is a test error"
        e = Exception(error_message)
        result = util.handle_error(e)
        expected_result = (error_message, http.client.BAD_REQUEST, {"Content-Type": "text/plain"})
        self.assertEqual(result, expected_result) 

if __name__ == "__main__": # pragma: no cover
    unittest.main()