def string_sequence(n: int) -> str:
    if n < 0 or n == None:
        return "Invalid input"
    else:
        return ' '.join(str(x) for x in range(n + 1))
import unittest

class Test(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()