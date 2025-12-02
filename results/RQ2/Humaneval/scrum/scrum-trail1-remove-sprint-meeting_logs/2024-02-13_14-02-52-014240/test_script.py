def search(lst):
    frequency_map = {}
    max_frequency_number = -1
    for num in lst:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
        if frequency_map[num] >= num:
            if num > max_frequency_number:
                max_frequency_number = num
    return max_frequency_number
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()