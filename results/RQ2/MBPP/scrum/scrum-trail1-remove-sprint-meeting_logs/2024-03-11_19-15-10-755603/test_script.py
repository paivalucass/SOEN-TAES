def max_sum_list(lists):
    if not lists:
        raise ValueError("Input list is empty")

    for sublist in lists:
        if not sublist:
            raise ValueError("Sublists cannot be empty")

    max_sum_list = lists[0]
    max_sum = sum(max_sum_list)

    for sublist in lists:
        current_sum = sum(sublist)
        if current_sum > max_sum:
            max_sum_list = sublist
            max_sum = current_sum

    return max_sum_list
import unittest

class Test(unittest.TestCase):
    def test_max_sum_list(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()