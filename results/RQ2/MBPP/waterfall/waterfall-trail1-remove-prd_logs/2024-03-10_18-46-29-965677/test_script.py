def left_insertion(a, x):
    if not a or x is None:
        return "Invalid input: List cannot be empty and element cannot be None"
    
    start = 0
    end = len(a)
    
    while start < end:
        mid = (start + end) // 2
        if a[mid] < x:
            start = mid + 1
        else:
            end = mid
    
    return start

assert left_insertion([1,2,4,5],6)==4
import unittest

class Test(unittest.TestCase):
    def test_left_insertion(self):
        self.assertEqual(left_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()