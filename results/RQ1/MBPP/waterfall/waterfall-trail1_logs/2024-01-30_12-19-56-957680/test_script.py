def find_Max_Num(arr):
    if not all(isinstance(x, int) and x >= 0 for x in arr):
        raise ValueError("Input list should contain only non-negative integers")
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    arr.sort(reverse=True)
    return int(''.join(map(str, arr)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()