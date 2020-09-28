import cal_code
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculator.add(1, 5)
        self.assertEqual(result, 6)
        
    def test_subtraction(self):
        result = calculator.subtract(3,2)
        self.assertEqual(result, 5)
        
        
if __name__ == '__main__':
    unittest.main()
