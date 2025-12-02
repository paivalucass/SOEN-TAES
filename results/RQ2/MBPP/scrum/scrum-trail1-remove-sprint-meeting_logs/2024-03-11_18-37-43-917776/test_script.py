def flatten_list(input_list):
    result = []
    for i in input_list:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

if __name__ == '__main__':
    unittest.main()