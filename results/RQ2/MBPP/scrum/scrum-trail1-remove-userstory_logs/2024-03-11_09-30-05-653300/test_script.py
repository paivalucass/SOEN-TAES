def max_sum_list(lists):
    if not lists or not all(isinstance(x, list) for x in lists):
        return "Invalid input: Please provide a non-empty list of lists"

    max_sum_list = []
    max_sum = 0

    for sub_list in lists:
        if sum(sub_list) > max_sum:
            max_sum = sum(sub_list)
            max_sum_list = sub_list

    return max_sum_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()