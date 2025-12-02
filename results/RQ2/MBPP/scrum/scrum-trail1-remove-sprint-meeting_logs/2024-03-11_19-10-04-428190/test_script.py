def check_expression(exp):
    stack = []
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in exp:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack:
                return False
            if stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            return False

    return not stack
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression('{()}[{}]'), True)

if __name__ == '__main__':
    unittest.main()