def car_race_collision(n: int):
    return n*(n-1)//2
import unittest

class TestCarRaceCollision(unittest.TestCase):
    def test_collision_count(self):
        self.assertEqual(car_race_collision(2), 1)
        self.assertEqual(car_race_collision(3), 3)
        self.assertEqual(car_race_collision(5), 10)
        self.assertEqual(car_race_collision(10), 45)

if __name__ == '__main__':
    unittest.main()

# The expected output is the number of collisions for a given n. In this case, the function should return n*(n-1)//2. The test script checks whether the output of the function matches the expected output for various values of n.