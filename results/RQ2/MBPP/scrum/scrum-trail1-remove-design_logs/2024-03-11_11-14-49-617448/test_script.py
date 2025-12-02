def check_expression(exp):
    stack = []
    brackets_map = {")": "(", "}": "{", "]": "["}
    for char in exp:
        if char in brackets_map.values():
            stack.append(char)
        else:
            if not stack:
                return False
            if brackets_map[char] != stack.pop():
                return False
    if stack:
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression('{()}[{}]'), True)

if __name__ == '__main__':
    unittest.main()