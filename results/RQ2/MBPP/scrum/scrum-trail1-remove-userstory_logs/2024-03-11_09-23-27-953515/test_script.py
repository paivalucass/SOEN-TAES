def multiply_elements(test_tup):
    if not all(isinstance(x, (int, float)) for x in test_tup):
        raise ValueError("Input tuple should contain only numbers")
    if len(test_tup) < 2:
        raise ValueError("Input tuple should contain at least two elements")

    result_tuple = tuple(test_tup[i] * test_tup[i+1] for i in range(len(test_tup) - 1))
    return result_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply_elements((1, 5, 7, 8, 10)), (5, 35, 56, 80))

if __name__ == '__main__':
    unittest.main()