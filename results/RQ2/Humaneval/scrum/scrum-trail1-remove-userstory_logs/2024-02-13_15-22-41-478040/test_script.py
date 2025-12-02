def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not isinstance(lst, list):
        return "Error: Input is not a list"
    
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)

if __name__ == '__main__':
    unittest.main()