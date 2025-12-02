def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        raise ValueError("Invalid lengths of operator and operand lists")
    
    expression = ""
    for i in range(len(operand)):
        if i < len(operand) - 1:
            expression += str(operand[i]) + operator[i]
        else:
            expression += str(operand[i])
    
    result = eval(expression)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()