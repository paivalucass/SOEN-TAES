def merge(lst):
    if not all(isinstance(sub_list, list) and len(sub_list) == 2 for sub_list in lst):
        return "Error: Invalid input data"
    
    output = [[], []]
    for sub_list in lst:
        output[0].append(sub_list[0])
        output[1].append(sub_list[1])
    return output
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]), [['x', 'a', 'm'], ['y', 'b', 'n']])

if __name__ == '__main__':
    unittest.main()