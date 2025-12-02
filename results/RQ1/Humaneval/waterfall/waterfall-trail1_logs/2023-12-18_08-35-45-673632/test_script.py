def generate_integers(a, b):
    even_numbers = []
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        return "Input validation failed: a and b must be positive integers"
    start = min(a, b)
    end = max(a, b)
    for num in range(start, end+1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
import unittest

class Test(unittest.TestCase):
    def test_generate_integers(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])

if __name__ == '__main__':
    unittest.main()