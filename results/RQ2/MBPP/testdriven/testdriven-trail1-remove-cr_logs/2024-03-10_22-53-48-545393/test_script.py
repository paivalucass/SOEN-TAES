def mul_even_odd(list1):
    even_num = None
    odd_num = None
    if len(list1) == 0:
        raise Exception("Input list is empty")
    for num in list1:
        if num % 2 == 0 and even_num is None:
            even_num = num
        elif num % 2 != 0 and odd_num is None:
            odd_num = num
        if even_num is not None and odd_num is not None:
            return even_num * odd_num
    raise Exception("Either even or odd number not found in the list")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()