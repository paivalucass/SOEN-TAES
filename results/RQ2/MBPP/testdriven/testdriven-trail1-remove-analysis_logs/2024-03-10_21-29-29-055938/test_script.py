def check_expression(exp):
    brackets_map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []

    for char in exp:
        if char in brackets_map:
            stack.append(char)
        elif char in brackets_map.values():
            if not stack:
                return False
            else:
                top = stack.pop()
                if brackets_map[top] != char:
                    return False

    return not stack
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression('{()}[{}]'), True)

if __name__ == '__main__':
    unittest.main()