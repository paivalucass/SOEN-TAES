def find_tuples(test_list, K):
    '''
    Write a function to find tuples which have all elements divisible by k from the given list of tuples.
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
    '''
    result = []
    for tup in test_list:
        if all(elem % K == 0 for elem in tup):
            result.append(tup)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()