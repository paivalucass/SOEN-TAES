def car_race_collision(n: int):
    return n * (n - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(3), 6)

if __name__ == '__main__':
    unittest.main()