def reverse_delete(s, c):
    result_string = ''
    for char in s:
        if char not in c:
            result_string += char
    return (result_string, result_string == result_string[::-1])
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))

    def test2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test3(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()