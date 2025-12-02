def min_Jumps(steps, d):
    x, y = steps
    distance = ((x**2 + y**2)**0.5) * d
    return distance

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Jumps((3, 4), 11), 3.5)

if __name__ == '__main__':
    unittest.main()