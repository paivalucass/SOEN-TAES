def find_sum(arr):
    if not isinstance(arr, list):
        return "Error: Input is not a list"
    
    for element in arr:
        if not isinstance(element, int):
            return "Error: Input list contains non-integer elements"
    
    non_repeated = [x for x in arr if arr.count(x) == 1]
    sum_non_repeated = sum(non_repeated)
    return sum_non_repeated

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()