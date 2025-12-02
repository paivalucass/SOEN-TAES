def search(lst):
    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    greatest_integer = -1
    for num, count in frequency_dict.items():
        if num <= count:
            greatest_integer = max(greatest_integer, num)
    
    return greatest_integer
import unittest

class Test(unittest.TestCase):
    def test_search_1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_search_2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_search_3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()