from queue import PriorityQueue
from typing import List

class Car:
    def __init__(self, position: int, direction: str):
        self.position = position
        self.direction = direction

    def __lt__(self, other):
        return self.position < other.position

def car_race_collision(n: int) -> int:
    left_cars = PriorityQueue()
    right_cars = PriorityQueue()
    collisions = 0
    
    for _ in range(n):
        left_cars.put(Car(0, 'left'))
        right_cars.put(Car(10**9, 'right'))
    
    while not left_cars.empty() and not right_cars.empty():
        if left_cars.queue[0] < right_cars.queue[0]:
            left_cars.get()
        else:
            collisions += 1
            right_cars.get()
    
    return collisions

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(5), 0)

if __name__ == '__main__':
    unittest.main()