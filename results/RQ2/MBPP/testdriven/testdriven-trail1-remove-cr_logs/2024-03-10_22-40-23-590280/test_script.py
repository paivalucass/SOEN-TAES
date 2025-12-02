def Find_Max(lst): 
    max_length = 0
    max_element = None
    for sub_list in lst:
        if isinstance(sub_list, list):
            if len(sub_list) > max_length:
                max_length = len(sub_list)
                max_element = sub_list
    return max_element

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()