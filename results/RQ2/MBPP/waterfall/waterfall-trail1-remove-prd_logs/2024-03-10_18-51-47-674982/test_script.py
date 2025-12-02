def add_pairwise(test_tup):
    if not isinstance(test_tup, tuple):
        return "Error: Invalid input"
    result = [test_tup[i] + test_tup[i+1] for i in range(0, len(test_tup)-1, 2)]
    if len(test_tup) % 2 != 0:
        result.append(test_tup[-1])
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_pairwise((1, 5, 7, 8, 10)), (6, 12, 15, 18))

if __name__ == '__main__':
    unittest.main()