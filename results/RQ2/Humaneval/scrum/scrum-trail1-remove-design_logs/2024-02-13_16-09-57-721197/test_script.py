def calculate_frequency(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

def search(lst):
    frequency = calculate_frequency(lst)
    result = -1
    for num in set(lst):
        if num > 0 and frequency[num] >= num:
            result = max(result, num)
    return result
import unittest

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_case2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_case3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()