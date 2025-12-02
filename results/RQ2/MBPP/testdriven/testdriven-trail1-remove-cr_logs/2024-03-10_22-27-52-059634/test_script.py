def find_Max_Num(arr):
    import re
    
    if not arr:
        return "Invalid input"
    
    for num in arr:
        if not str(num).isdigit():
            return "Invalid input"
    
    arr.sort(reverse=True)
    return int(''.join(map(str, arr)))

# Test the function
assert find_Max_Num([1,2,3]) == 321
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1, 2, 3]), 321)

if __name__ == '__main__':
    unittest.main()