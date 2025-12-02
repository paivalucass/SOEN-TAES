def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    def error_checking(n):
        if n < 0:
            return "Error: Invalid input"
        elif n == 0:
            return 1
        elif n > 10:
            return "Error: Input out of range"
        else:
            return None

    error = error_checking(n)
    if error:
        return error

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()