def extract_singly(test_list):
    unique_numbers_set = set()
    for sublist in test_list:
        for number in sublist:
            unique_numbers_set.add(number)
    return unique_numbers_set
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]), {3, 4, 5, 7, 1})

if __name__ == '__main__':
    unittest.main()