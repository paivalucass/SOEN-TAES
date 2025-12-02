def find_Max_Num(arr) :
    '''Write a python function to find the largest number that can be formed with the given list of digits.
    assert find_Max_Num([1,2,3]) == 321'''
    # Check if the input array is valid
    if not all(isinstance(x, int) for x in arr) or len(arr) == 0 or any(isinstance(x, str) for x in arr):
        return "Invalid input"
    
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Handle the case when the input array contains only negative numbers or when all elements are zero
    if arr[-1] < 0:
        arr = arr[1:] + [arr[0]]
    elif arr.count(0) == len(arr):
        return 0
    
    return int(''.join(str(i) for i in arr))

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()