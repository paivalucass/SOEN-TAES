def add_pairwise(test_tup):
    if not isinstance(test_tup, tuple):
        raise ValueError("Error: Invalid input. Input should be a tuple.")

    if len(test_tup) < 2:
        raise ValueError("Error: Invalid input. Tuple should have at least 2 elements.")

    if not all(isinstance(elem, (int, float)) for elem in test_tup):
        raise ValueError("Error: Elements of the tuple are not numeric")

    result = [test_tup[i] + test_tup[i+1] for i in range(len(test_tup) - 1)]
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_pairwise((1, 5, 7, 8, 10)), (6, 12, 15, 18))

if __name__ == '__main__':
    unittest.main()