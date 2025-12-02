def flatten_list(list1):
    if not isinstance(list1, list):
        raise TypeError("Input must be a list")

    flattened_list = []
    stack = list1[::-1]  # change list1[:] to list1[::-1]

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current[::-1])  # change stack.extend(current) to stack.extend(current[::-1])
        else:
            flattened_list.append(current)

    return flattened_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

if __name__ == '__main__':
    unittest.main()