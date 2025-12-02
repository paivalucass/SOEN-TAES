def do_algebra(operator, operand):
    def build_expression(operators, operands):
        expression = ""
        for i in range(len(operators)):
            expression += str(operands[i]) + " " + operators[i] + " "
        expression += str(operands[-1])
        return expression

    def evaluate_expression(expression):
        try:
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"

    if len(operator) != len(operand) - 1:
        return "Error: Length of operator list should be one less than the length of the operand list"
    if len(operand) < 2 or len(operator) < 1:
        return "Error: Operand list should have at least two operands and operator list should have at least one operator"

    algebraic_expression = build_expression(operator, operand)
    result = evaluate_expression(algebraic_expression)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()