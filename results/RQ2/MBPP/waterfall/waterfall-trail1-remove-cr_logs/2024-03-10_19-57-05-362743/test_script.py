def check_occurrences(test_list):
    occurrences_dict = {}
    for item in test_list:
        if isinstance(item, tuple) and all(isinstance(i, int) for i in item):
            if item in occurrences_dict:
                occurrences_dict[item] += 1
            else:
                occurrences_dict[item] = 1
    return occurrences_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]), {(3, 1): 1, (1, 3): 1, (2, 5): 1, (5, 2): 1, (6, 3): 1})

if __name__ == '__main__':
    unittest.main()