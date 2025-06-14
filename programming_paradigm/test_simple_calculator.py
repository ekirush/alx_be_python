from simple_calculator import SimpleCalculator #import class
import unittest


class Test_Class(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calculator = SimpleCalculator()
        
        
    def test_add(self):
        addition = self.calculator.add(5,3)
        self.assertEqual(addition,8)
        
    def test_subtract(self):
        subtraction = self.calculator.subtract(10,2)
        self.assertEqual(subtraction,8)
    def test_multiply(self):
        multiply = self.calculator.multiply(10,2)
        self.assertEqual(multiply,20)
    def test_divide(self):
        division = self.calculator.divide(10,2)
        self.assertEqual(division,5)
    def test_divide_by_zero(self):
        division = self.calculator.divide(10, 0)
        self.assertEqual(division, None)

# if __name__ == '__main__':
#     unittest.main()
