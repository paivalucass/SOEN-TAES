def count_first_elements(test_tup):
    if isinstance(test_tup, tuple):
        for i in range(len(test_tup)):
            if isinstance(test_tup[i], tuple):
                return i
        return 0
    else:
        return TypeError
import unittest

class Test(unittest.TestCase):
    def test_count_first_elements(self):
        self.assertEqual(count_first_elements((1, 5, 7, (4, 6), 10)), 3)

if __name__ == '__main__':
    unittest.main()