def sort_third(l: list):
    temp = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    return [temp.pop(0) if i % 3 == 0 else l[i] for i in range(len(l))]

import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()