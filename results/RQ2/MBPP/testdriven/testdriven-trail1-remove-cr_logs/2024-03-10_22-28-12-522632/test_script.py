def recursive_list_sum(data_list, memo={}):
    total_sum = 0
    
    if not isinstance(data_list, list):
        raise TypeError("Input is not a list")
    
    for element in data_list:
        if isinstance(element, list):
            total_sum += recursive_list_sum(element, memo)
        elif isinstance(element, int):
            total_sum += element
        else:
            raise ValueError("Non-numerical element found in input list")
    
    return total_sum

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3,4],[5,6]]), 21)

if __name__ == '__main__':
    unittest.main()