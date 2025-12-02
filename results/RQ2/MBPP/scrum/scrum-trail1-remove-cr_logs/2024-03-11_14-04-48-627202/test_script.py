def mul_even_odd(list1):
    even = None
    odd = None
    has_even = False
    has_odd = False
    for num in list1:
        if num % 2 == 0 and even is None:
            even = num
            has_even = True
        elif num % 2 != 0 and odd is None:
            odd = num
            has_odd = True
        if has_even and has_odd:
            break
    if has_even and has_odd:
        return even * odd
    else:
        return "Input list does not contain at least one even and one odd number"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()