def mul_even_odd(list1):
    if not list1:
        return "Error: Empty input list"
    
    even_num = None
    odd_num = None
    
    for num in list1:
        if not isinstance(num, int):
            return "Error: Non-integer inputs present in the list"
        if num < 0:
            return "Error: Negative numbers present in the list"
        if num % 2 == 0 and even_num is None:
            even_num = num
        elif num % 2 != 0 and odd_num is None:
            odd_num = num
        if even_num is not None and odd_num is not None:
            return even_num * odd_num
    
    if even_num is None or odd_num is None:
        return "Error: No even or odd numbers in the list"
    
    if len(list1) > 13:
        return "Error: List size exceeds limit"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()