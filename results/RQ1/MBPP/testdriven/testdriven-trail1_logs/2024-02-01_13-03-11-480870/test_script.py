def diff_even_odd(list1):
    even = []
    odd = []
    for num in list1:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even[0] - odd[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()