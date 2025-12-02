def reverse_delete(s, to_delete):
    result = ''
    for char in s:
        if char not in to_delete:
            result += char
    return (result, result == result[::-1])
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse_delete('abcde', 'ae'), ('bcd', False))

    def test_2(self):
        self.assertEqual(reverse_delete('abcdef', 'b'), ('acdef', False))

    def test_3(self):
        self.assertEqual(reverse_delete('abcdedcba', 'ab'), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()