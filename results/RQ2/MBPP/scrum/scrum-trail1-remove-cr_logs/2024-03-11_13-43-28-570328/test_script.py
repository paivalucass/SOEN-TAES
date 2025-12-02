def diff_even_odd(list1):
    even = None
    odd = None
    for num in list1:
        if even is None and num % 2 == 0:
            even = num
        elif odd is None and num % 2 != 0:
            odd = num
        if even is not None and odd is not None:
            break
    if even is not None and odd is not None:
        return abs(even - odd)
    else:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()