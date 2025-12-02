def car_race_collision(n: int):
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    
    return n * (n - 1) // 2

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(3), 3)

if __name__ == '__main__':
    unittest.main()