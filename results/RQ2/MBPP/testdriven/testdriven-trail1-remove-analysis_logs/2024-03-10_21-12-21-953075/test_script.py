def frequency(arr, target):
    if not isinstance(arr, list):
        return "Error: Input is not a list"
    if not all(isinstance(i, int) for i in arr):
        return "Error: List contains non-integer elements"
    
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1,2,3], 4), 0)

if __name__ == '__main__':
    unittest.main()