def tuple_str_int(test_str):
    if test_str[0] != '(' or test_str[-1] != ')':
        raise ValueError("Invalid tuple format")

    integers = [int(x) for x in test_str[1:-1].split(',')]

    result_tuple = tuple(integers)

    return result_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()