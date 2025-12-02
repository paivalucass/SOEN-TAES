def max_sum_list(lists):
    if not lists:
        return "Input list is empty"

    max_sum = float('-inf')
    max_sum_sublist = []

    for sub_list in lists:
        if not all(isinstance(x, int) for x in sub_list):
            return "Input list contains non-numeric elements"
        
        sum_of_sublist = sum(sub_list)
        if sum_of_sublist > max_sum:
            max_sum = sum_of_sublist
            max_sum_sublist = sub_list
    
    return max_sum_sublist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()