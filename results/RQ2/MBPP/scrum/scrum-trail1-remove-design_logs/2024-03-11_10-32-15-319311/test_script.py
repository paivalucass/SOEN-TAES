def add_nested_tuples(test_tup1, test_tup2):
    try:
        assert len(test_tup1) == len(test_tup2), "Input tuples are not of the same length"
        return tuple(tuple(sum(pair) for pair in zip(subtuple1, subtuple2)) for subtuple1, subtuple2 in zip(test_tup1, test_tup2))
    except AssertionError as e:
        return e
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((7, 10), (7, 14), (3, 10), (8, 13)))

if __name__ == '__main__':
    unittest.main()