def reverse_delete(s, c):
    if not s or not c:
        return ("Input strings or characters to be removed cannot be empty", False)
    
    c_set = set(c)
    
    result = []
    for char in s:
        if char not in c_set:
            result.append(char)
    
    result_str = ''.join(result)
    is_palindrome = result_str == result_str[::-1]
    
    return (result_str, is_palindrome)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_delete('abcde', 'ae'), ('bcd', False))
        self.assertEqual(reverse_delete('abcdef', 'b'), ('acdef', False))
        self.assertEqual(reverse_delete('abcdedcba', 'ab'), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()