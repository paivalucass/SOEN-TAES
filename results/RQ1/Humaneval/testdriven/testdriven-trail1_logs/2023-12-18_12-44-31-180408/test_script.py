def even_odd_count(number):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    try:
        if not isinstance(number, int):
            raise ValueError
    except ValueError:
        return "Error Handling"
    
    even_count = 0
    odd_count = 0
    number = abs(number)
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number //= 10
    
    return (even_count, odd_count)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))

if __name__ == '__main__':
    unittest.main()