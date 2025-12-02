def find_equal_tuple(input_list):
    if len(input_list) < 2:
        return True
    else:
        length = len(input_list[0])
        return all(len(tup) == length for tup in input_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()