import cal_code
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculator.add(2, 5)
        self.assertEqual(result, 7)
        
    def test_subtraction(self):
        result = calculator.subtract(5,2)
        self.assertEqual(result, 3)
        
        
if __name__ == '__main__':
    unittest.main()
