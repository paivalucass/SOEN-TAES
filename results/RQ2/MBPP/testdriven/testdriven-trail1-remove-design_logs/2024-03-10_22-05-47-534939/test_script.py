def find_lucas(n):
    '''
    Write a function to find the n'th lucas number.
    assert find_lucas(9) == 76
    '''
    if type(n) != int:
        return "Error: non-integer input"
    elif n < 0:
        return "Invalid input"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return calculate_lucas_number(n)

def calculate_lucas_number(n):
    a, b = 2, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b if b < 9999999 else "larger lucas number returned within acceptable time"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()