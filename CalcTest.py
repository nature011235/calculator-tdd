import unittest
from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)  # Expect 5 - 2 = 3

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(3, 4)
        self.assertEqual(result, 12)  # Expect 3 * 4 = 12

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)  # Expect 10 / 2 = 5

    def test_divide_float_result(self):
        calc = Calculator()
        result = calc.divide(5, 2)
        self.assertEqual(result, 2.5)  # Expect 5 / 2 = 2.5

    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(5, 0)  # Should raise ValueError


if __name__ == "__main__":
    unittest.main()
