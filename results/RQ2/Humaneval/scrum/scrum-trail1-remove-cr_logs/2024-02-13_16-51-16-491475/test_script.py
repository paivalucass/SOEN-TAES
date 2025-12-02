def sort_third(l: list):
    new_list = l.copy()
    for i in range(len(new_list)):
        if i % 3 == 0:
            new_list[i] = sorted(new_list[i])
    return new_list

import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()