def extract_singly(test_list):
    if not all(isinstance(sublist, list) for sublist in test_list):
        raise TypeError("Input must be a list of lists")
    
    flat_list = {item for sublist in test_list for item in sublist}
    return set(flat_list)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]), {3, 4, 5, 7, 1})

if __name__ == '__main__':
    unittest.main()