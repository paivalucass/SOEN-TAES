def area_tetrahedron(side):
    if not isinstance(side, (int, float)) or side <= 0:
        raise ValueError("Side length must be a positive number")

    area = (3 ** 0.5) * side ** 2
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()