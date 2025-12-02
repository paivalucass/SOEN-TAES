def find_lucas(n):
    '''Write a function to find the n'th lucas number.'''
    # Add your code here
    lucas_numbers = [2, 1]
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            lucas_numbers.append(lucas_numbers[i-1] + lucas_numbers[i-2])
        return lucas_numbers[n]

assert find_lucas(9) == 76
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()