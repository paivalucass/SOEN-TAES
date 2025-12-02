def area_tetrahedron(side_length):
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        return "Error: Invalid input for side length"

    area = (side_length ** 2) * ((3 ** 0.5) / 4)
    return round(area, 15)
import unittest

class Test(unittest.TestCase):
    def test_area_tetrahedron(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()