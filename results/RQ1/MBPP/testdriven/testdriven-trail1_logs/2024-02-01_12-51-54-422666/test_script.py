def add_pairwise(test_tup):
    '''
    Write a function to find the pairwise addition of the neighboring elements of the given tuple.
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    '''
    if not isinstance(test_tup, tuple):
        raise ValueError("Input should be a tuple")
    for val in test_tup:
        if not isinstance(val, (int, float)):
            raise ValueError("Tuple should contain only numeric values")
    result = []
    for i in range(len(test_tup) - 1):
        result.append(test_tup[i] + test_tup[i + 1])
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_pairwise((1, 5, 7, 8, 10)), (6, 12, 15, 18))

if __name__ == '__main__':
    unittest.main()