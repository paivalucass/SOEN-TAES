def radian_degree(degree):
    import math
    
    radian = None
    try:
        radian = math.radians(degree)
    except ValueError:
        return "Error: Invalid input"
    
    return radian
import math
import unittest

class Test(unittest.TestCase):
    def test_radian_degree(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()