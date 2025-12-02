def median_trapezium(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Input values must be non-negative")
    
    if base1 == base2:
        raise ValueError("Base1 and base2 must be distinct")
    
    median = (base1 + base2) / 2
    return median
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()