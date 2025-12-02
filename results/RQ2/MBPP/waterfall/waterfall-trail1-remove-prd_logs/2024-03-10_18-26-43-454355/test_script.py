def find_equal_tuple(Input):
    if not isinstance(Input, list) or not all(isinstance(t, tuple) for t in Input):
        return False
    if len(Input) == 0:
        return False  # Input list is empty
    first_tuple_length = len(Input[0])
    for tuple_item in Input:
        if len(tuple_item) != first_tuple_length:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()