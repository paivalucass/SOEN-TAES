def remove_parenthesis(items):
    result = ''
    open_paren_count = 0
    for char in items:
        if char == '(': 
            open_paren_count += 1
        elif char == ')' and open_paren_count > 0:
            open_paren_count -= 1
        elif open_paren_count == 0:
            result += char
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_parenthesis('python (chrome)'), 'python')

if __name__ == '__main__':
    unittest.main()