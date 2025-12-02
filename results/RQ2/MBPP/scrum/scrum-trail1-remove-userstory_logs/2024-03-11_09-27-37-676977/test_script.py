def find_sum(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        return 0
    
    non_repeated_elements = set()
    for element in arr:
        if arr.count(element) == 1:
            non_repeated_elements.add(element)
    
    return sum(non_repeated_elements)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()