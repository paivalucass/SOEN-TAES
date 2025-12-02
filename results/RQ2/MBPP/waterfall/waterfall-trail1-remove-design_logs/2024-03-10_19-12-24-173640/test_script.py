def otherside_rightangle(w, h):
    import math
    if isinstance(w, (int, float)) and isinstance(h, (int, float)):
        if w > 0 and h > 0:
            return math.sqrt(w**2 + h**2)
        else:
            return "Invalid input"
    else:
        return "Invalid input"
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()