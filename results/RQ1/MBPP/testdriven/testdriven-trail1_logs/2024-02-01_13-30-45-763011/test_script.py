def remove_nested(test_tup):
    '''Write a function to remove tuples from the given tuple.'''
    result = []
    for item in test_tup:
        if isinstance(item, tuple):
            result.extend(item)
        else:
            result.append(item)
    return tuple(filter(lambda x: not isinstance(x, tuple), result))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()