def minimum(a, b):  
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: Invalid input"
    
    if a < b:
        return a
    else:
        return b
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()