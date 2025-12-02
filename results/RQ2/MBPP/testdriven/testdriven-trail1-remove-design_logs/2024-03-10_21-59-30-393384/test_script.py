def circle_circumference(r):
    import math

    try:
        if type(r) not in [int, float]:
            raise TypeError("Error: Invalid input type")
        elif r < 0:
            raise ValueError("Error: Negative input value")
        elif r == 0:
            raise ValueError("Error: Zero input value")
        else:
            return round(2 * math.pi * r, 2)
    except (TypeError, ValueError) as e:
        return str(e)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(circle_circumference(10), 62.830000000000005, delta=0.001)

if __name__ == '__main__':
    unittest.main()