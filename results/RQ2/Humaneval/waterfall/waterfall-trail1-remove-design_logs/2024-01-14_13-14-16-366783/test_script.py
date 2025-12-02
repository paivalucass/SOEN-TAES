def is_sum_of_two_equal_to_third(num1, num2, num3):
    if all(isinstance(x, int) for x in [num1, num2, num3]):
        if num1 == num2 + num3 or num2 == num1 + num3 or num3 == num1 + num2:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(any_int(5, 2, 7), True)
        self.assertEqual(any_int(3, 2, 2), False)
        self.assertEqual(any_int(3, -2, 1), True)
        self.assertEqual(any_int(3.6, -2.2, 2), False)

if __name__ == '__main__':
    unittest.main()