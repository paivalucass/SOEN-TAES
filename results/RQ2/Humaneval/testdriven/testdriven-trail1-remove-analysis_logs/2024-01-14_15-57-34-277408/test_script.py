def solution(lst):
    total_sum = 0
    for index, num in enumerate(lst):
        if index % 2 == 0 and num % 2 != 0:
            total_sum += num
    return total_sum
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