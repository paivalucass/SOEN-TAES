def multiple_to_single(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]
    else:
        try:
            result = int(''.join(map(str, L)))
            return result
        except ValueError:
            return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()