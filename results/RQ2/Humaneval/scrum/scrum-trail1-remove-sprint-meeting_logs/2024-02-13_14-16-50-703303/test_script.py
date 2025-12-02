def reverse_delete(s, c):
    if not s or not c:
        return "Invalid input: s and c should not be empty."

    for char in c:
        if char not in s:
            return "Invalid input: Characters in c are not present in s."

    result_string = "".join([char for char in s if char not in c])
    is_palindrome = result_string == result_string[::-1]

    return (result_string, is_palindrome)
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