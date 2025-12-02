def check_expression(exp):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in exp:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

assert check_expression("{()}[{}]") == True
assert check_expression("[()]{}") == True
assert check_expression("{(})") == False
assert check_expression("[({))]") == False
assert check_expression("{{[[()]]}}") == True
assert check_expression("[{}]()") == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression('{()}[{}]'), True)

if __name__ == '__main__':
    unittest.main()