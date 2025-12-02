def remove_parenthesis(items):
    result = ''
    count = 0
    for char in items:
        if char == '(': count += 1
        elif char == ')' and count > 0: count -= 1
        elif count == 0: result += char
    return result
import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis(["python (chrome)"]), ["python"])

if __name__ == '__main__':
    unittest.main()