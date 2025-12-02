def car_race_collision(n: int):
    return n * 10
  
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(10), 100)

if __name__ == '__main__':
    unittest.main()