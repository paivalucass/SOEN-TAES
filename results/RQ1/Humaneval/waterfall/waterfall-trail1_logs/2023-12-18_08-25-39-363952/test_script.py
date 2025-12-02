def reverse_delete(s, c):
    result_string = ''.join([char for char in s if char not in c])
    palindrome_check = result_string == result_string[::-1]
    return (result_string, palindrome_check)
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))

    def test_example2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_example3(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()