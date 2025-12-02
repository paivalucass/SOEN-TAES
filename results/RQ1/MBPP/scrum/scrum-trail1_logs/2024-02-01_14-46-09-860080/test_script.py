def find_lists(input_tuple):
    count = 0
    for elem in input_tuple:
        if isinstance(elem, list):
            count += 1
            count += find_lists(elem)  # recursive call for nested lists
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])), 2)

if __name__ == '__main__':
    unittest.main()