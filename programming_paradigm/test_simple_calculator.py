from simple_calculator import SimpleCalculator #import class
import unittest


class Test_Class(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
        
        
    def test_addition(self):
        self.assertEqual(self.calc.add(5,3),8)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,2),8)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10,2),20)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(10,2),5)
        
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(10, 0), None)

# if __name__ == '__main__':
#     unittest.main()
