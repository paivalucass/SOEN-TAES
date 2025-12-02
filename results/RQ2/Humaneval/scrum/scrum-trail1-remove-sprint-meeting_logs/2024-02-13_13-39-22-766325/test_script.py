def string_sequence(n: int) -> str:
    if n < 0:
        return "Invalid input: n must be a non-negative integer"
    result = " ".join(str(i) for i in range(n+1))
    return result.strip()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()