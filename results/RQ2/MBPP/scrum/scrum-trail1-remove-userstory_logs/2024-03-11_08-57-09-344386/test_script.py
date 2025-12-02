def find_lists(Input):
    if not isinstance(Input, tuple):
        raise ValueError("Input is not a tuple")

    count = 0

    for element in Input:
        if isinstance(element, list):
            count += 1

    return count
import unittest

class Test(unittest.TestCase):
    def test_find_lists(self):
        self.assertEqual(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])), 2)

if __name__ == '__main__':
    unittest.main()