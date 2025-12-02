def area_tetrahedron(side):
    if not isinstance(side, (int, float)):
        return "Error: Side must be a numeric value"
    if side <= 0:
        return "Error: Side must be a positive number"
    
    area = (3 ** 0.5) * (side ** 2)
    return round(area, 15)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()