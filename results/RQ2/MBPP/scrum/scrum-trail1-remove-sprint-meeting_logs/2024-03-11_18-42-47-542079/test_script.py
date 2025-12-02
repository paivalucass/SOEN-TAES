def max_Product(arr):
    if len(arr) < 2:
        return "Array should have at least 2 elements"

    arr.sort()

    max_product = arr[0] * arr[1]

    for i in range(len(arr)-1):
        product = arr[i] * arr[i+1]
        if product > max_product:
            max_product = product
            result = (arr[i], arr[i+1])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7,8))

if __name__ == '__main__':
    unittest.main()