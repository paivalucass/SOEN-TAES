def get_ludic(n):
    '''Write a function to get all lucid numbers smaller than or equal to a given integer.'''
    lucid_numbers = []
    if n < 1:
        return lucid_numbers
    for num in range(1, n+1):
        if num == 1:
            lucid_numbers.append(num)
        else:
            is_lucid = True
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    is_lucid = False
                    break
            if is_lucid:
                lucid_numbers.append(num)
    return lucid_numbers

import unittest

class Test(unittest.TestCase):
    def test_get_ludic(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()