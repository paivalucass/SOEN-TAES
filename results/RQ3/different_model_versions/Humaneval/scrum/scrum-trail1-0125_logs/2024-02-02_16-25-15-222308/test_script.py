def solution(lst):
    if not isinstance(lst, list) or not all(isinstance(num, int) for num in lst):
        raise ValueError("Input must be a non-empty list of integers")
    
    odd_elements_in_even_positions = [num for index, num in enumerate(lst) if num % 2 != 0 and index % 2 == 0]
    return sum(odd_elements_in_even_positions)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)

if __name__ == '__main__':
    unittest.main()