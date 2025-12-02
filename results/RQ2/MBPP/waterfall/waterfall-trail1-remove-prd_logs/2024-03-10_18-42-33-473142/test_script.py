import math

def polar_rect(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        return "Error: Invalid input"
    if x < 0:
        return "Invalid input for polar coordinates: x must be non-negative"
    
    rect_x = round(x * math.cos(y), 10)
    rect_y = round(x * math.sin(y), 10)
    
    return (rect_x, rect_y)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()