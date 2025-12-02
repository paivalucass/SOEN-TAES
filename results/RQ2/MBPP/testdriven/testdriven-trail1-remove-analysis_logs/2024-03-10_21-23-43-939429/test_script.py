def perfect_squares(a, b):
    '''Write a function to find perfect squares between two given numbers.'''
    result = []
    for num in range(a, b+1):
        root = num ** 0.5
        if int(root + 0.5) ** 2 == num:
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()