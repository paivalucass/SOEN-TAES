def function_under_test(s):
    result = ''
    has_letters = False
    for char in s:
        if char.isalpha():
            has_letters = True
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    if not has_letters:
        result = result[::-1]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('1234'), '4321')
        self.assertEqual(function_under_test('ab'), 'AB')
        self.assertEqual(function_under_test('#a@C'), '#A@c')

if __name__ == '__main__':
    unittest.main()