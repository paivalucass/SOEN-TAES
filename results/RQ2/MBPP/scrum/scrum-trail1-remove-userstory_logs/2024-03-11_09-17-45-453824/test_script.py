def diff_even_odd(input_list):
    even_found = False
    odd_found = False
    diff = 0
    
    for num in input_list:
        if num % 2 == 0 and not even_found:
            even = num
            even_found = True
        elif num % 2 != 0 and not odd_found:
            odd = num
            odd_found = True
        
        if even_found and odd_found:
            diff = abs(even - odd)
            break
    
    return diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()