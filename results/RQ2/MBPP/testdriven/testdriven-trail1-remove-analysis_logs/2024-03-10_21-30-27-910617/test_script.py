def remove_nested(test_tup):
    if not isinstance(test_tup, tuple):
        raise TypeError("Invalid input: Input is not a tuple")
    result = []
    for item in test_tup:
        if isinstance(item, tuple):
            result.extend(remove_nested(item))
        else:
            result.append(item)
    return tuple([x for x in result if x is not None])
import unittest

class Test(unittest.TestCase):
    def test_remove_nested(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()