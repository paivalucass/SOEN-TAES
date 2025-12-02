def validate_inputs(operator, operand):
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list should be one less than the length of the operand list")
    if len(operand) < 2 or any(num < 0 for num in operand):
        raise ValueError("Operand list should contain at least two non-negative integers")
    if len(operator) < 1:
        raise ValueError("Operator list should have at least one operator")


def build_expression(operator, operand):
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += operator[i] + str(operand[i+1])
    return expression


def evaluate_expression(expression):
    safe_operators = {'+': 'add', '-': 'sub', '*': 'mul', '//': 'floordiv', '**': 'pow'}
    for op in safe_operators:
        expression = expression.replace(op, safe_operators[op])
    result = eval(expression)
    return str(result)


def do_algebra(operator, operand):
    validate_inputs(operator, operand)
    expression = build_expression(operator, operand)
    result = evaluate_expression(expression)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()