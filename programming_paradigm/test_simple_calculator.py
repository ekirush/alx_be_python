from simple_calculator import SimpleCalculator #import class
import unittest


class Test_Class(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
        
        
    def test_addition(self):
        addition = self.calc.add(5,3)
        self.assertEqual(addition,8)
        
    def test_subtract(self):
        subtraction = self.calc.subtract(10,2)
        self.assertEqual(subtraction,8)
        
    def test_multiply(self):
        multiply = self.calc.multiply(10,2)
        self.assertEqual(multiply,20)
        
    def test_divide(self):
        division = self.calc.divide(10,2)
        self.assertEqual(division,5)
        
    def test_divide_by_zero(self):
        division = self.calc.divide(10, 0)
        self.assertEqual(division, None)

# if __name__ == '__main__':
#     unittest.main()
