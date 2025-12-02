def multiple_to_single(L):
    if not L:
        return 0
    for num in L:
        if not isinstance(num, int):
            return "Invalid input"
    return int("".join(map(str, L)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()