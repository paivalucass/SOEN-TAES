import math

def area_tetrahedron(side_length):
    if side_length <= 0:
        return "Invalid Input"
    else:
        return round((math.sqrt(3) * side_length * side_length), 15)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()