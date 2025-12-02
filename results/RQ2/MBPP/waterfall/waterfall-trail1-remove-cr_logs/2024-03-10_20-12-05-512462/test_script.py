def merge(lst):
    if not all(isinstance(sublst, list) and len(sublst) == 2 for sublst in lst):
        raise ValueError("Input must be a list of lists with two elements each")
    
    result = [list(x) for x in zip(*lst)]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]), [['x', 'a', 'm'], ['y', 'b', 'n']])

if __name__ == '__main__':
    unittest.main()