def find_equal_tuple(input_list):
    if not isinstance(input_list, list) or not all(isinstance(item, tuple) for item in input_list):
        return "Error: Input is not a list of tuples"

    length = len(input_list[0])
    for item in input_list:
        if len(item) != length:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()