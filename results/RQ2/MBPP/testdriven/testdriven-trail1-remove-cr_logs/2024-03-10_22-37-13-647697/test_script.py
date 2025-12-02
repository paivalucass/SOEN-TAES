def max_length(list1):
    if not list1:
        return "Error: Empty Input"

    max_len = 0
    max_list = []

    for inner_list in list1:
        if not isinstance(inner_list, list):
            return "Error: Input is not a list of lists"

        if len(inner_list) > max_len:
            max_len = len(inner_list)
            max_list = inner_list

    return (max_len, max_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()