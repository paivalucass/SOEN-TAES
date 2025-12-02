def area_tetrahedron(side):
    if not isinstance(side, (int, float)) or side <= 0:
        raise ValueError("The side length of the tetrahedron must be a positive number")

    area = (side ** 2) * (6 ** 0.5) / 12
    return round(area * (3 ** 0.5), 15)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()