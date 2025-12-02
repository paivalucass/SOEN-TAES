def multiply_elements(test_tup):
    if len(test_tup) < 2 or len(test_tup) > 10:
        raise ValueError("Input tuple length should be between 2 and 10")
    for num in test_tup:
        if not isinstance(num, (int, float)):
            raise TypeError("Input tuple should only contain numeric elements")
    result = tuple(test_tup[i] * test_tup[i+1] for i in range(len(test_tup) - 1))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply_elements((1, 5, 7, 8, 10)), (5, 35, 56, 80))

if __name__ == '__main__':
    unittest.main()