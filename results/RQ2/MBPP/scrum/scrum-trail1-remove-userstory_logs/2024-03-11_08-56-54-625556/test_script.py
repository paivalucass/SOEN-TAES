def extract_singly(test_list):
    result_set = set()
    
    def flatten_list(input_list):
        for item in input_list:
            if isinstance(item, int):
                result_set.add(item)
            else:
                flatten_list(item)
    
    flatten_list(test_list)
    return result_set

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]), set([3, 4, 5, 7, 1]))

if __name__ == '__main__':
    unittest.main()