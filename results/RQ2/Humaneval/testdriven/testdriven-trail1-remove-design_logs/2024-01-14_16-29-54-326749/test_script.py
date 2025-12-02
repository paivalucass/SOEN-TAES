def generate_integers(a, b):
    if type(a) != int or type(b) != int or a <= 0 or b <= 0:
        return "Error: Both a and b must be positive integers"
    if a == b:
        return [] if a % 2 == 0 else []
    if a > b:
        a, b = b, a
    return [i for i in range(a, b+1) if i % 2 == 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])

if __name__ == '__main__':
    unittest.main()