def next_Perfect_Square(N):
    try:
        if not isinstance(N, int) or N < 0:
            raise ValueError("Invalid input. Please provide a positive integer.")
        
        i = N + 1
        while True:
            if (i**0.5).is_integer():
                return i
            else:
                i += 1
    except ValueError as ve:
        return ve
import unittest

class Test(unittest.TestCase):
    def test_next_Perfect_Square(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()