import cal_code
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = cal_code.add(1, 5)
        self.assertEqual(result, 6)
        
    def test_subtraction(self):
        result = cal_code.subtract(3,2)
        self.assertEqual(result, 1)
        
        
if __name__ == '__main__':
    unittest.main()
