def car_race_collision(n: int):
    return max(0, (n*(n-1)) // 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(3), 3)
        self.assertEqual(car_race_collision(4), 6)
        self.assertEqual(car_race_collision(5), 10)

if __name__ == '__main__':
    unittest.main()