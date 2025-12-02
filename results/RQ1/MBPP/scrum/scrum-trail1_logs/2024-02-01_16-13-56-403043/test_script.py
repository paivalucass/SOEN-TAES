def diff_even_odd(list1):
    even_found = False
    odd_found = False
    diff = 0

    for num in list1:
        if num % 2 == 0 and not even_found:
            first_even = num
            even_found = True
        elif num % 2 != 0 and not odd_found:
            first_odd = num
            odd_found = True
        
        if even_found and odd_found:
            diff = abs(first_even - first_odd)
            break
    
    if not even_found or not odd_found:
        raise ValueError("The input list does not contain both even and odd numbers")

    return diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()