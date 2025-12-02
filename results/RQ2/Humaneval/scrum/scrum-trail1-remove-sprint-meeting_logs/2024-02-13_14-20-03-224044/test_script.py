def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        product = 1
        sum_of_magnitudes = 0
        for num in arr:
            if num > 0:
                product *= 1
                sum_of_magnitudes += num
            elif num < 0:
                product *= -1
                sum_of_magnitudes += abs(num)
            else:
                product *= 0
        return product * sum_of_magnitudes
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test2(self):
        self.assertEqual(prod_signs([0, 1]), 0)

    def test3(self):
        self.assertEqual(prod_signs([]), None)

if __name__ == '__main__':
    unittest.main()