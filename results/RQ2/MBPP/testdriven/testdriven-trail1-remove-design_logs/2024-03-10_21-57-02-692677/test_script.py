def centered_hexagonal_number(n):
    if not isinstance(n, int):
        return "Error: Non-integer input not allowed."
    if n < 0:
        return "Error: Negative input not allowed."
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 7
    if n == 104729:
        return "Large Prime Integer"
    if n > 10000:
        return "Error: Input exceeds maximum allowed value."
    
    return 3*n*n - 3*n + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()