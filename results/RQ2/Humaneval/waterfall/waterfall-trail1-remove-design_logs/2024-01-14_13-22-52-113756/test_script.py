def solve(s):
    result = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    if not any(char.isalpha() for char in result):
        return result[::-1]
    return result[::-1]
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(solve("1234"), "4321")

    def test2(self):
        self.assertEqual(solve("ab"), "AB")

    def test3(self):
        self.assertEqual(solve("#a@C"), "#A@c")

if __name__ == '__main__':
    unittest.main()