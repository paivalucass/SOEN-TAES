def do_algebra(operators, operands):
    if len(operators) != len(operands) - 1:
        return "Error: Length of operator list should be one less than the length of operand list"

    valid_operators = ['+', '-', '*', '//', '**']
    if any(op not in valid_operators for op in operators):
        return "Error: Invalid operator"

    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += operands[i+1]
        elif operators[i] == '*':
            result *= operands[i+1]
        elif operators[i] == '-':
            result -= operands[i+1]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()