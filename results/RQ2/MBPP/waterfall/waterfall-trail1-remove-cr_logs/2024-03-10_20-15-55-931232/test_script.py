def area_tetrahedron(side):
    if not isinstance(side, (int, float)) or side <= 0:
        return "Error: Invalid input for side"
    area = (side ** 2) * ((3 ** 0.5) / 4)
    return round(area, 15) if side > 0 else "Error: Length of side must be positive"
import unittest

class Test(unittest.TestCase):
    def test_area_tetrahedron(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()