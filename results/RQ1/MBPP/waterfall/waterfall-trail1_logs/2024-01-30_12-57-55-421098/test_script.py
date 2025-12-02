def max_length(list1):
    if not list1 or not all(isinstance(i, list) for i in list1):
        raise ValueError("Input list of lists is empty or contains elements that are not lists")

    max_len_list = max(list1, key=len)
    max_length = len(max_len_list)

    return max_length, max_len_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()