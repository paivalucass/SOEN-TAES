def check_occurences(test_list):
    '''Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.'''
    occurrences_dict = {}
    for item in test_list:
        if item in occurrences_dict:
            occurrences_dict[item] += 1
        else:
            occurrences_dict[item] = 1
    return occurrences_dict

# Rewrite code using defaultdict
from collections import defaultdict

def check_occurences(test_list):
    occurrences_dict = defaultdict(int)
    for item in test_list:
        occurrences_dict[item] += 1
    return dict(occurrences_dict)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]), {(3, 1): 1, (1, 3): 1, (2, 5): 1, (5, 2): 1, (6, 3): 1})

if __name__ == '__main__':
    unittest.main()