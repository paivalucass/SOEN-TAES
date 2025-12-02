def sum_squares(lst):
    total = 0
    if not isinstance(lst, (list, tuple, set)):
        raise ValueError("Input must be a list, tuple, or set")
    for num in lst:
        if not isinstance(num, (int, float)):
            raise ValueError("List must contain numbers only")
        rounded_num = int(num) if num > 0 else math.ceil(num)
        total += rounded_num**2
    return total
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_squares([1,2,3]), 14)

    def test_2(self):
        self.assertEqual(sum_squares([1,4,9]), 98)

    def test_3(self):
        self.assertEqual(sum_squares([1,3,5,7]), 84)

    def test_4(self):
        self.assertEqual(sum_squares([1.4,4.2,0]), 29)

    def test_5(self):
        self.assertEqual(sum_squares([-2.4,1,1]), 6)

if __name__ == '__main__':
    unittest.main()