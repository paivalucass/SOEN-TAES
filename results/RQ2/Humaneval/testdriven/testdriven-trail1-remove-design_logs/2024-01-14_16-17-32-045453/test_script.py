def car_race_collision(n: int):
    left_cars = [(i, "left") for i in range(n)]
    right_cars = [(i, "right") for i in range(n)]
    
    collisions = 0
    for l_car in left_cars:
        for r_car in right_cars:
            if l_car[0] > r_car[0] and l_car[1] == "left" and r_car[1] == "right":
                collisions += 1
    
    return collisions
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(3), 3)

if __name__ == '__main__':
    unittest.main()