def multiply_elements(test_tup):
    result = []
    for i in range(len(test_tup) - 1):
        result.append(test_tup[i] * test_tup[i+1])
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply_elements((1, 5, 7, 8, 10)), (5, 35, 56, 80))

if __name__ == '__main__':
    unittest.main()