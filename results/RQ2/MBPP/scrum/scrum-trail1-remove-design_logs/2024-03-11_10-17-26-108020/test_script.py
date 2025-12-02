def check_occurences(test_list):
    '''Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.'''
    occurences = {}
    for item in test_list:
        if item in occurences:
            occurences[item] += 1
        else:
            occurences[item] = 1
    return occurences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]), {(3, 1): 1, (1, 3): 1, (2, 5): 1, (5, 2): 1, (6, 3): 1})

if __name__ == '__main__':
    unittest.main()