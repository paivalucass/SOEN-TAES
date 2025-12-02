def check_occurences(test_list):
    occurrences = {}
    if not isinstance(test_list, list):
        return occurrences

    for tpl in test_list:
        if not isinstance(tpl, tuple):
            continue

        if tpl in occurrences:
            occurrences[tpl] += 1
        else:
            occurrences[tpl] = 1
    
    return occurrences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]), {(3, 1): 1, (1, 3): 1, (2, 5): 1, (5, 2): 1, (6, 3): 1})

if __name__ == '__main__':
    unittest.main()