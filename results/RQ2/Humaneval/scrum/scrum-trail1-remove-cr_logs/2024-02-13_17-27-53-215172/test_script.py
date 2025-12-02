def do_algebra(operators, operands):
    result = operands[0]
    for i in range(1, len(operands)):
        if operators[i-1] == '+':
            result += operands[i]
        elif operators[i-1] == '*':
            result *= operands[i]
        elif operators[i-1] == '-':
            result -= operands[i]
        elif operators[i-1] == '//':
            result //= operands[i]
        elif operators[i-1] == '**':
            result **= operands[i]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()