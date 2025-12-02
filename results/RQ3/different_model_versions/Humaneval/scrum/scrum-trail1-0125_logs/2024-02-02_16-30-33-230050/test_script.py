def solve(s):
    result = []
    for char in s:
        if char.isalpha():
            result.append(char.swapcase())
        else:
            result.append(char)
    if not any(char.isalpha() for char in s):
        return s[::-1]
    return ''.join(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve("1234"), "4321")
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("#a@C"), "#A@c")

if __name__ == '__main__':
    unittest.main()