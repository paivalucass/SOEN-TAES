def find_lists(Input):
    list_count = 0
    for element in Input:
        if isinstance(element, list):
            list_count += 1

    return list_count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])), 2)

if __name__ == '__main__':
    unittest.main()