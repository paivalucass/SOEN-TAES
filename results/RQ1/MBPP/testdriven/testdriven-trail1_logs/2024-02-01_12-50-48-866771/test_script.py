from itertools import combinations

def combinations_list(list1):
    result = []
    for i in range(len(list1) + 1):
        result.extend(list(combinations(list1, i)))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_list(['orange', 'red', 'green', 'blue']), [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']])

if __name__ == '__main__':
    unittest.main()