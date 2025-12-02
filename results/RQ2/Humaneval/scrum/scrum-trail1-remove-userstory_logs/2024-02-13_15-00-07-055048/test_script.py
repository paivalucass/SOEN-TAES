def string_sequence(n: int) -> str:
    if not isinstance(n, int) or n < 0:
        return ""
    if n == 0:
        return "0"
    else:
        return ' '.join([str(i) for i in range(n+1)])
import unittest

class Test(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()