def find_lists(Input):
    count = 0
    for item in Input:
        if isinstance(item, list):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])), 2)

if __name__ == '__main__':
    unittest.main()