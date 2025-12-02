def find_solution(a, b, n):
    import math
    if a == 0 or b == 0 or n % math.gcd(a, b) != 0:
        return None

    gcd = math.gcd(a, b)
    x = 1
    y = (n - a*x) / b

    if y.is_integer() and y >= 0:
        return (int(x * gcd), int(y * gcd))
    else:
        return None

# Test
assert find_solution(2, 3, 7) == (2, 1)
import unittest

class Test(unittest.TestCase):
    def test_find_solution(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()