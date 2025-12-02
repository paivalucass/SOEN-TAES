def flatten_list(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input is not a list")

    result = []
    stack = [input_list]

    while stack:
        current = stack.pop()
        for item in reversed(current):
            if isinstance(item, list):
                stack.append(item)
            else:
                result.append(item)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

if __name__ == '__main__':
    unittest.main()