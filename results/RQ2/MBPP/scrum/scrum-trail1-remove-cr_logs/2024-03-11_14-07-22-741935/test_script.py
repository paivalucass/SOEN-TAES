def max_sum_list(lists):
    if not lists:
        raise ValueError("Input list of lists is empty")

    max_sum = float('-inf')
    max_list = []

    for lst in lists:
        if not lst:
            raise ValueError("Input list contains an empty sub-list")
        
        current_sum = sum(lst)
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = lst
            
    return max_list
import unittest

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()