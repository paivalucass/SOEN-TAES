def unique_Element(arr):
    if not isinstance(arr, list):
        raise TypeError("Input should be a list")
    
    for element in arr:
        if not isinstance(element, (int, float)):
            raise TypeError("List should only contain numeric elements")
    
    unique_set = set(arr)
    
    return len(unique_set) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()