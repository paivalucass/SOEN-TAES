def odd_Equivalent(s, n):
    '''Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
    assert odd_Equivalent("011001",6) == 3'''
    if not isinstance(s, str) or not all(char in '01' for char in s):
        raise ValueError("Input s must be a binary string")

    if not isinstance(n, int):
        raise ValueError("Input n must be an integer")

    s_len = len(s)
    n = n % s_len

    odd_count = sum(1 for char in s[-n:] if char == '1')
    even_count = s_len - n - odd_count

    if n % 2 == 0:
        return even_count
    else:
        return odd_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()