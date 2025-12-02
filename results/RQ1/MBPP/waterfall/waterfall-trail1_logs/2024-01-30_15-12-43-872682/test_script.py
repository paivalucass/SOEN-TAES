def right_insertion(a, x):
    if not a:
        raise ValueError("Input list is empty")
    if x is None:
        raise ValueError("Value to be inserted is not provided")
        
    low = 0
    high = len(a) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return low
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()