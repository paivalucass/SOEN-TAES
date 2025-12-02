def car_race_collision(n: int):
    return min(n, 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(1), 0)
        self.assertEqual(car_race_collision(2), 1)
        self.assertEqual(car_race_collision(3), 3)
        self.assertEqual(car_race_collision(5), 10)

if __name__ == '__main__':
    unittest.main()