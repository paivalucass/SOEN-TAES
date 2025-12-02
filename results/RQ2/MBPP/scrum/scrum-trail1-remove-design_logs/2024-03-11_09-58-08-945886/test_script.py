def find_equal_tuple(Input):
    if not all(isinstance(tup, tuple) for tup in Input):
        return "Error"
    return len(set(len(tup) for tup in Input)) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()