def jacobsthal_num(n):
    '''Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...'''
    # Check for negative input or non-integer input
    if n < 0 or not isinstance(n, int):
        return "Error"
    # Base cases
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    # Calculate jacobsthal number using iterative approach
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, 2*a + b
        return b
# Test case
assert jacobsthal_num(5) == 11
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()