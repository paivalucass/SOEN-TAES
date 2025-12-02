def check_occurences(test_list):
    occurrences = {}
    if isinstance(test_list, list) and all(isinstance(item, tuple) for item in test_list):
        for item in test_list:
            if item in occurrences:
                occurrences[item] += 1
            else:
                occurrences[item] = 1
        return occurrences
    else:
        return "Invalid input: Please provide a list of tuples."
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]), {(3, 1): 1, (1, 3): 1, (2, 5): 1, (5, 2): 1, (6, 3): 1})

if __name__ == '__main__':
    unittest.main()