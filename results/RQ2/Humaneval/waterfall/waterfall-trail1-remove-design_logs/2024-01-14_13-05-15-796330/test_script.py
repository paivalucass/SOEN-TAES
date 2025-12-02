from typing import Union

def greatest_common_divisor(a: int, b: int) -> Union[int, str]:
    """
    Return the greatest common divisor of two integers a and b
    """
    if not isinstance(a, int) or not isinstance(b, int):
        return "Error: Invalid input, both parameters should be integers"

    if a == 0 and b == 0:
        return "Error: Invalid input, both parameters should be non-zero integers"

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b
    return a

# Test the function with various input values
assert greatest_common_divisor(10, 5) == 5
assert greatest_common_divisor(14, 28) == 14
assert greatest_common_divisor(0, 5) == 5
assert greatest_common_divisor(-6, -9) == 3
assert greatest_common_divisor(0, 0) == "Error: Invalid input, both parameters should be non-zero integers"
import unittest

class Test(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()