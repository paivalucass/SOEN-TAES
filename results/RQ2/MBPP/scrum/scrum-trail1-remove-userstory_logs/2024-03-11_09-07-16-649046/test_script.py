def maximum(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Input parameters are not valid numbers")
    
    max_num = max(a, b)
    
    return max_num
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()