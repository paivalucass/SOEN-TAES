def merge(lst):
    result = [[], []]
    for sub_list in lst:
        result[0].append(sub_list[0])
        result[1].append(sub_list[1])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]), [['x', 'a', 'm'], ['y', 'b', 'n']])

if __name__ == '__main__':
    unittest.main()