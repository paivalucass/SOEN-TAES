def radian_degree(degree):
    import math
    try:
        radians = math.radians(degree)
        return radians
    except Exception as e:
        return "Error message"
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()