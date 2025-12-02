def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return None
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while b:
        a, b = b, a % b
    return a

# Rewrite the code to pass all test cases
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return None
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()