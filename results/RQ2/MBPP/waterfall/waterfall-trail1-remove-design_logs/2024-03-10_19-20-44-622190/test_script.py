def diff_even_odd(list1):
    even_num = None
    odd_num = None
    for num in list1:
        if num % 2 == 0:
            even_num = num
            break
    for num in list1:
        if num % 2 != 0:
            odd_num = num
            break
    if even_num is None or odd_num is None:
        return "None"
    return abs(even_num - odd_num)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()