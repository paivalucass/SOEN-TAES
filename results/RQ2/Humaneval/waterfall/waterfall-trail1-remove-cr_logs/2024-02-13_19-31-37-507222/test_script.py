def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a <= 0 or b <= 0:
        return "Invalid input: Both integers should be positive"

    start = min(a, b)
    end = max(a, b)
    result = [i for i in range(start, end+1) if i % 2 == 0]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(2, 8), [2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()