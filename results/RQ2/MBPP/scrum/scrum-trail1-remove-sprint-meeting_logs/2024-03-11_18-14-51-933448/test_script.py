def find_equal_tuple(input):
    if not input or not all(isinstance(item, tuple) for item in input):
        raise ValueError("Input list should not be empty and should only contain tuples")

    first_tuple_length = len(input[0])
    for tup in input[1:]:
        if len(tup) != first_tuple_length:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()