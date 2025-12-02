def solution(lst):
    odd_elements_in_even_positions = [lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0]
    return sum(odd_elements_in_even_positions)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)

if __name__ == '__main__':
    unittest.main()