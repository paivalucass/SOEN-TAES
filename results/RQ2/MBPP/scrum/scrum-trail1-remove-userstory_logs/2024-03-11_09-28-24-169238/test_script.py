def mul_even_odd(input_list):
    if not input_list:
        return "Error: Input list is empty"
    
    even_found = False
    odd_found = False
    product = 0
    
    for num in input_list:
        if num % 2 == 0 and not even_found:
            even_number = num
            even_found = True
        
        if num % 2 != 0 and not odd_found:
            odd_number = num
            odd_found = True
            
        if even_found and odd_found:
            product = even_number * odd_number
            break
    
    if even_found and odd_found:
        return product
    else:
        return "Error: List does not contain both even and odd numbers"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()