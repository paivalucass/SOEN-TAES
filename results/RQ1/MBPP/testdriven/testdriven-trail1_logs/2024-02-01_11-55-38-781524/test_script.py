def find_tuples(test_list, K):
    '''
    Write a function to find tuples which have all elements divisible by K from the given list of tuples.
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
    '''

    # Input validation
    if not isinstance(test_list, list) or not all(isinstance(t, tuple) for t in test_list):
        raise ValueError("Input validation failed: test_list must be a list of tuples")

    if not isinstance(K, int):
        raise ValueError("Input validation failed: K must be an integer")

    if not test_list or K == 0:
        raise ValueError("Error handling failed: test_list cannot be empty and K cannot be 0")

    # Finding tuples with all elements divisible by K
    result = [t for t in test_list if all(x % K == 0 for x in t)]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()