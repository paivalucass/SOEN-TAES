def find_lists(input_tuple):
    count = 0
    if not isinstance(input_tuple, tuple):
        raise ValueError("Input is not a tuple")

    for item in input_tuple:
        if isinstance(item, list):
            count += 1

    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])), 2)

if __name__ == '__main__':
    unittest.main()