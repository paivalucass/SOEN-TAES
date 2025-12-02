def find_equal_tuple(Input):
    if not isinstance(Input, list) or not all(isinstance(item, tuple) for item in Input):
        raise ValueError("Input must be a list of tuples")

    if not Input:
        return False

    tuple_length = len(Input[0])
    for item in Input:
        if len(item) != tuple_length:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()