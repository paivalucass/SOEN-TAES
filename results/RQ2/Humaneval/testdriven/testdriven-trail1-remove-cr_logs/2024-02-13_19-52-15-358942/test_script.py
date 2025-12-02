import math

def sum_squares(lst):
    total = 0
    for num in lst:
        num = int(num) if num >= 0 else math.ceil(num)
        total += num * num
    return total
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_squares([1,2,3]), 14)
    
    def test2(self):
        self.assertEqual(sum_squares([1,4,9]), 98)
    
    def test3(self):
        self.assertEqual(sum_squares([1,3,5,7]), 84)
    
    def test4(self):
        self.assertEqual(sum_squares([1.4,4.2,0]), 29)
    
    def test5(self):
        self.assertEqual(sum_squares([-2.4,1,1]), 6)

if __name__ == '__main__':
    unittest.main()