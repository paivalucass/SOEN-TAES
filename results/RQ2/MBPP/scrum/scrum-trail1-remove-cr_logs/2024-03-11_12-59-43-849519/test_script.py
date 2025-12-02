def division_elements(test_tup1: tuple, test_tup2: tuple) -> tuple:
    result = ()
    try:
        for i in range(len(test_tup1)):
            if test_tup2[i] != 0:
                result += (test_tup1[i] / test_tup2[i],)
            else:
                result += (None,)
        return result
    except TypeError:
        return "Error: Input tuples must contain numerical values only."
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9), (5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()