def find_equal_tuple(Input):
    if not Input:
        raise ValueError("Input list is empty")

    if not all(isinstance(tup, tuple) for tup in Input):
        raise TypeError("Input list contains non-tuple elements")

    length = len(Input[0])
    for tup in Input:
        if len(tup) != length:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()