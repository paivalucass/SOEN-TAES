def last(arr, x):
    if arr != sorted(arr):
        arr.sort()
    
    if x not in arr:
        return -1
    
    last_index = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            last_index = i
    
    return last_index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()