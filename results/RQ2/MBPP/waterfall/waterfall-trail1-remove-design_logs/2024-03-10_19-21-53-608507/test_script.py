def min_Jumps(steps, d):
    if len(steps) != 2 or d <= 0:
        return 'Invalid input values'

    x, y = steps
    distance_to_cover = (x ** 2 + y ** 2) ** 0.5

    if distance_to_cover == 0:
        return 'Cannot cover zero distance'

    jumps_required = d / distance_to_cover
    return round(jumps_required, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Jumps((3,4), 11), 3.5)

if __name__ == '__main__':
    unittest.main()