def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]

    result = ''
    for char in s:
        if char.isalpha():
            result += char.swapcase()
        else:
            result += char

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve('1234'), '4321')
        self.assertEqual(solve('ab'), 'AB')
        self.assertEqual(solve('#a@C'), '#A@c')

if __name__ == '__main__':
    unittest.main()