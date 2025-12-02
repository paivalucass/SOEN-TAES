def unique_product(list_data):
    if not list_data:
        return 0

    unique_numbers = set(list_data)
    product = 1
    for num in unique_numbers:
        if num < 0:
            return -1
        product *= num
    return product
import unittest

class Test(unittest.TestCase):
    def test_unique_product(self):
        self.assertEqual(unique_product([10, 20, 30, 40, 20, 50, 60, 40]), 720000000)

if __name__ == '__main__':
    unittest.main()