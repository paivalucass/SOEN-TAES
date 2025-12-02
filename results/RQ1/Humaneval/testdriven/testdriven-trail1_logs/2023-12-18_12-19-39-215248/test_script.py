def string_sequence(n: int) -> str:
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid input"
    if n > 1000000:
        return "Error: Input value too large"
    
    return ' '.join(map(str, range(n+1)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()