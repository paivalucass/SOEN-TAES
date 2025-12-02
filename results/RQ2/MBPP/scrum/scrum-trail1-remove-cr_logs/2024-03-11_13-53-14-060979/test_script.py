def remove_parenthesis(items):
    result = ''
    inside_parenthesis = 0
    for char in items:
        if char == '(': inside_parenthesis += 1
        elif char == ')' and inside_parenthesis > 0: inside_parenthesis -= 1
        elif inside_parenthesis == 0: result += char
    return result.strip()

import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis("python (chrome)"), "python")

if __name__ == '__main__':
    unittest.main()