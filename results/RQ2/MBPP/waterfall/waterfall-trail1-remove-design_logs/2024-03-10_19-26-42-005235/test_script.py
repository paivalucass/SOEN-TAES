def mul_even_odd(list1):
    even_num = None
    odd_num = None
    
    for num in list1:
        if even_num is None and num % 2 == 0:
            even_num = num
        elif odd_num is None and num % 2 != 0:
            odd_num = num
        if even_num is not None and odd_num is not None:
            break
    
    if even_num is None or odd_num is None:
        return 0  # Meaningful value when there are no even or odd numbers in the list
    else:
        return even_num * odd_num

assert mul_even_odd([1,3,5,7,4,1,6,8])==4
assert mul_even_odd([2,4,6,8])==0  # Ensure it handles cases with no odd numbers
assert mul_even_odd([1,3,5,7])==0  # Ensure it handles cases with no even numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()