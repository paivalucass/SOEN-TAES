def eat(number, need, remaining):
    total_eaten_carrots = number + need
    carrots_left_after_meal = max(0, remaining - need)
    return [total_eaten_carrots, max(0, remaining - total_eaten_carrots)]

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])
    
    def test2(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])
    
    def test3(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])
    
    def test4(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()