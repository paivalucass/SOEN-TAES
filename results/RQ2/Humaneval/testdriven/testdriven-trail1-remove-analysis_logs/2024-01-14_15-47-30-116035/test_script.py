from typing import List

def car_race_collision(left_positions: List[int], right_positions: List[int]) -> int:
    collisions = 0
    for left_pos in left_positions:
        for right_pos in right_positions:
            if left_pos > right_pos:
                collisions += 1
    return collisions
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(3), 3)

if __name__ == '__main__':
    unittest.main()