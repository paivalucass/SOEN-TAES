def max_sum_list(lists):
    if not all(isinstance(lst, list) for lst in lists):
        raise ValueError("Input should be a list of lists")

    for lst in lists:
        if not all(isinstance(x, int) for x in lst):
            raise ValueError("Inner lists should only contain integers")

    max_sum = float('-inf')
    max_list = []

    for lst in lists:
        if sum(lst) > max_sum:
            max_sum = sum(lst)
            max_list = lst

    return max_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()