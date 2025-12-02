def solution(lst):
    return sum(lst[i] for i in range(len(lst)) if i % 2 == 1 and lst[i] % 2 != 0)
import unittest

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)

if __name__ == '__main__':
    unittest.main()