def do_algebra(operators, operands):
    if len(operators) < 1 or len(operands) < 2:
        return "Error: Invalid input"
    
    valid_operators = ['+', '-', '*', '//', '**']
    for op in operators:
        if op not in valid_operators:
            return f"Error: Invalid operator '{op}' in the operator list"
    
    result = operands[0]
    operator_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
        '**': lambda x, y: x ** y
    }
    for i in range(1, len(operands)):
        if operators[i-1] in operator_dict:
            result = operator_dict[operators[i-1]](result, operands[i])
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()