def solution(lst):
    sum_odd_at_even_pos = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum_odd_at_even_pos += lst[i]
    return sum_odd_at_even_pos
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
    
    def test2(self):
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
    
    def test3(self):
        self.assertEqual(solution([30, 13, 24, 321]), 0)

if __name__ == '__main__':
    unittest.main()