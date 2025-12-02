def get_ludic(n):
    '''Function to get all lucid numbers smaller than or equal to a given integer.'''
    result = []
    for num in range(1, n + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            result.append(num)
    return result

assert get_ludic(10) == [1, 2, 3, 5, 7]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()