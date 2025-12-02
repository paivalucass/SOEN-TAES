def do_algebra(operators, operands):
    if len(operators) != len(operands) - 1:
        raise ValueError("Invalid input for operator and operand")

    operator_map = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
        '**': lambda x, y: x ** y
    }

    result = operands[0]
    for i in range(len(operators)):
        if operators[i] not in operator_map:
            raise ValueError("Invalid operator")
        result = operator_map[operators[i]](result, operands[i + 1])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

if __name__ == '__main__':
    unittest.main()