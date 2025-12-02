def and_tuples(test_tup1, test_tup2):
    result = ()
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples should have the same length")
    for i in range(len(test_tup1)):
        if not isinstance(test_tup1[i], int) or not isinstance(test_tup2[i], int):
            raise ValueError("Input tuples should only contain integer elements")
        result += (test_tup1[i] & test_tup2[i],)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)), (0, 0, 2, 1))

if __name__ == '__main__':
    unittest.main()