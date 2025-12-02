def and_tuples(test_tup1, test_tup2):
    result = tuple(x & y for x, y in zip(test_tup1, test_tup2))
    return result

def test_and_tuples():
    assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    # Add more test cases to cover different scenarios and edge cases

test_and_tuples()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)), (0, 0, 2, 1))

if __name__ == '__main__':
    unittest.main()