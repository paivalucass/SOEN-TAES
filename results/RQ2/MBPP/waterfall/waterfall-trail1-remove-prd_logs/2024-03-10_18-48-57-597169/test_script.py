def find_combinations(test_list):
    result = [(tup[0] + tup[1], tup[0] + tup[1]) for tup in test_list]
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]), [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)])

if __name__ == '__main__':
    unittest.main()