def diff_even_odd(list1):
    def find_first_number(lst, even):
        for num in lst:
            if (even and num % 2 == 0) or (not even and num % 2 != 0):
                return num
        return None

    first_even = find_first_number(list1, True)
    first_odd = find_first_number(list1, False)

    if first_even is None or first_odd is None:
        return None
    else:
        return abs(first_even - first_odd)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()