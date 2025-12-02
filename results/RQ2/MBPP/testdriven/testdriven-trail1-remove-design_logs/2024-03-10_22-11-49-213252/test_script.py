def unique_product(list_data):
    unique_numbers_count = {}
    product = 1
    for num in list_data:
        if num in unique_numbers_count:
            unique_numbers_count[num] += 1
        else:
            unique_numbers_count[num] = 1
    for num, count in unique_numbers_count.items():
        product *= num
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_product([10, 20, 30, 40, 20, 50, 60, 40]), 720000000)

if __name__ == '__main__':
    unittest.main()