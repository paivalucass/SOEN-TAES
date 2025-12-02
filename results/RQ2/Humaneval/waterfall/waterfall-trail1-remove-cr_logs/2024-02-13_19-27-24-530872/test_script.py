def add_elements(arr, k):
    try:
        if len(arr) == 0:
            raise ValueError("Input array is empty")
        
        for num in arr:
            if not isinstance(num, int):
                raise ValueError("Input array contains non-integer values")
        
        sum_selected = 0
        count = 0
        for num in arr:
            if len(str(num)) <= 2 and count < k:
                sum_selected += num
                count += 1
        
        return sum_selected
    
    except ValueError as e:
        return str(e)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_elements([111,21,3,4000,5,6,7,8,9], 4), 24)

if __name__ == '__main__':
    unittest.main()