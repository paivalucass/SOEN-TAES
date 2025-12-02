def reverse_delete(s, c):
    result_string = ''.join([char for char in s if char not in c])
    is_palindrome = result_string == result_string[::-1]
    return (result_string, is_palindrome)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_delete('abcde', 'ae'), ('bcd', False))
        self.assertEqual(reverse_delete('abcdef', 'b'), ('acdef', False))
        self.assertEqual(reverse_delete('abcdedcba', 'ab'), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()