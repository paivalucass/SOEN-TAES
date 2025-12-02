def next_Perfect_Square(N):
    if N < 0 or not isinstance(N, int):
        return "Invalid Input"
    
    i = int(N ** 0.5) + 1
    while i ** 2 <= N:
        i += 1

    return i ** 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()