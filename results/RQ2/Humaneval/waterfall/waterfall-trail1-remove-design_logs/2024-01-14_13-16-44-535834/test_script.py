def reverse_delete(s,c):
    result = ''.join([char for char in s if char not in c])
    return (result, result == result[::-1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_delete('abcde', 'ae'), ('bcd', False))
        self.assertEqual(reverse_delete('abcdef', 'b'), ('acdef', False))
        self.assertEqual(reverse_delete('abcdedcba', 'ab'), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()