def do_algebra(operators, operands):
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += operands[i + 1]
        elif operators[i] == '-':
            result -= operands[i + 1]
        elif operators[i] == '*':
            result *= operands[i + 1]
        elif operators[i] == '/':
            result /= operands[i + 1]
        elif operators[i] == '**':
            result **= operands[i + 1]
    return result
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()