def extract_singly(test_list):
    if not all(isinstance(item, tuple) for item in test_list):
        raise ValueError("Input must be a list of lists")
    return set(num for sublist in test_list for num in sublist)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]), set([3, 4, 5, 7, 1]))

if __name__ == '__main__':
    unittest.main()