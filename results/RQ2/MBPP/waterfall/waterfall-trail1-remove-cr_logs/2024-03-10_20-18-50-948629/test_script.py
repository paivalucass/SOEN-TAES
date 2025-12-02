def mul_even_odd(list1):
    if not list1:
        raise ValueError("Input list is empty")
    
    even = None
    odd = None
    
    for num in list1:
        if num % 2 == 0 and even is None:
            even = num
        elif num % 2 != 0 and odd is None:
            odd = num
        
        if even is not None and odd is not None:
            break
    
    if even is None or odd is None:
        raise ValueError("Input list does not contain both even and odd numbers")
    
    return even * odd
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()