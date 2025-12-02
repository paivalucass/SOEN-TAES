def extract_singly(test_list):
    result_set = set()
    for sublist in test_list:
        if not isinstance(sublist, tuple):
            raise ValueError("Input is not a list of tuples")
        result_set.update(sublist)
    return result_set
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]), set([3, 4, 5, 7, 1]))

if __name__ == '__main__':
    unittest.main()