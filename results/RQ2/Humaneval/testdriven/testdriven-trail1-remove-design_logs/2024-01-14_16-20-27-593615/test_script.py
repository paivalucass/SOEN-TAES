def search(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    result = -1
    for key, value in frequency.items():
        if key == value and key > result:
            result = key
    
    return result
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()