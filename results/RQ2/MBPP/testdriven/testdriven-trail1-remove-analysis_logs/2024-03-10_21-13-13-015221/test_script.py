def check_occurences(test_list):
    from collections import Counter
    return dict(Counter(test_list))
import unittest

class Test(unittest.TestCase):
    def test_check_occurences(self):
        self.assertEqual(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]), {(3, 1): 1, (1, 3): 1, (2, 5): 1, (5, 2): 1, (6, 3): 1})

if __name__ == '__main__':
    unittest.main()