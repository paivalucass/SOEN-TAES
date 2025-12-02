def validate_input(operator, operand):
    if len(operator) != len(operand) - 1:
        return False
    if len(operand) < 2:
        return False
    if len(operator) < 1:
        return False
    for num in operand:
        if num < 0:
            return False
    return True

def build_expression(operator, operand):
    expression = ''
    for i in range(len(operator)):
        expression += str(operand[i]) + operator[i]
    expression += str(operand[-1]) 
    return expression

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except:
        return "Error: Invalid expression"

def do_algebra(operator, operand):
    if not operator:
        return "Error: Operator list is empty"
    if not operand:
        return "Error: Operand list is empty"
    if not validate_input(operator, operand):
        return "Error: Invalid input"
    expression = build_expression(operator, operand)
    result = evaluate_expression(expression)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()