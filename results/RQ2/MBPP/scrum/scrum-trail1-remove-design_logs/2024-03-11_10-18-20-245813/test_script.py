def next_Perfect_Square(N):
    if N < 0:
        return "Error"
    x = N + 1
    while True:
        root = x ** 0.5
        if root.is_integer():
            return x
        x += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()