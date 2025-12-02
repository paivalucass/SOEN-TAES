def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if not (isinstance(a, int) and isinstance(b, int)) or a > b:
        raise ValueError("Error: 'a' and 'b' should be valid integers and 'a' should be less than or equal to 'b'")
    if a % 2 != 0:
        a += 1
    if a > b:
        return []
    return list(range(a, b+1, 2))
import unittest

class Test(unittest.TestCase):
    def test_generate_integers(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])

if __name__ == '__main__':
    unittest.main()