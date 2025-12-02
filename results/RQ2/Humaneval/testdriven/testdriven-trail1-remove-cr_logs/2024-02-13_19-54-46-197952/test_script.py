def do_algebra(operator, operand):
    if len(operand) < 2 or len(operator) != len(operand) - 1:
        return "Invalid input"
    
    for op in operator:
        if op not in ['+', '-', '*', '//', '**']:
            return "Invalid operator: {}".format(op)

    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            if operand[i+1] == 0:
                return "Error: Division by zero"
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()