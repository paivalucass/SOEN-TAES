def find_lucas(n):
    '''Return the n'th Lucas number.'''
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        current_lucas_number = 2
        next_lucas_number = 1
        for _ in range(2, n + 1):
            current_lucas_number, next_lucas_number = next_lucas_number, current_lucas_number + next_lucas_number
        return next_lucas_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()