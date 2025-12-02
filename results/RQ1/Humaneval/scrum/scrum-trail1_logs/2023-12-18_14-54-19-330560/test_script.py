def string_sequence(n: int) -> str:
    try:
        if not isinstance(n, int):
            raise ValueError("Input parameter should be an integer")
        if n < 0:
            return ' '.join(str(i) for i in range(n, -1, -1))
        else:
            return ' '.join(str(i) for i in range(n + 1))
    except ValueError as e:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()