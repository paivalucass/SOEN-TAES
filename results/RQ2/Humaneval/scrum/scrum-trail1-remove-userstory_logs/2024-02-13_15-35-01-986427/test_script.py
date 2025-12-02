def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return "Error: The first input parameter 'a' must be less than or equal to the second input parameter 'b'."
    else:
        result = [i for i in range(a, b + 1) if i % 2 == 0]
        return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])

if __name__ == '__main__':
    unittest.main()