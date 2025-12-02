def merge(lst):
    if not lst or any(len(sublist) != 2 for sublist in lst):
        return "Invalid input"

    result = [[], []]
    for sub in lst:
        result[0].append(sub[0])
        result[1].append(sub[1])

    return result

import unittest

class Test(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]), [['x', 'a', 'm'], ['y', 'b', 'n']])

if __name__ == '__main__':
    unittest.main()