def find_lists(input_tuple):
    count = 0
    for item in input_tuple:
        if isinstance(item, list):
            count += 1
        elif isinstance(item, tuple):
            count += find_lists(item)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])), 2)

if __name__ == '__main__':
    unittest.main()