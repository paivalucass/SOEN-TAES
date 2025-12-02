def mul_even_odd(list1):
    even_number = None
    odd_number = None

    for num in list1:
        if num % 2 == 0 and even_number is None:
            even_number = num
        elif num % 2 != 0 and odd_number is None:
            odd_number = num
        if even_number is not None and odd_number is not None:
            break

    if even_number is None or odd_number is None:
        raise ValueError("Input list must contain at least one even and one odd number")

    return even_number * odd_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()