def circle_circumference(r: float) -> float:
    import math
    
    if not isinstance(r, (int, float)):
        return "Invalid input type"
    
    if r <= 0:
        return "Invalid input type"
    
    circumference = 2 * math.pi * r
    return round(circumference, 2)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(circle_circumference(10), 62.830000000000005, delta=0.001)

if __name__ == '__main__':
    unittest.main()