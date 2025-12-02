def add_pairwise(test_tup):
    if not test_tup:
        return "Error: Input tuple is empty"
    
    if len(test_tup) == 1:
        return test_tup

    for val in test_tup:
        if not isinstance(val, (int, float)):
            return "Error: Input tuple contains non-numeric values"

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