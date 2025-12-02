def combinations_list(list1):
    result = [[]]
    for element in list1:
        result += [i + [element] for i in result]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_list(['orange', 'red', 'green', 'blue']), [[], ['orange'], ['red'], ['orange', 'red'], ['green'], ['orange', 'green'], ['red', 'green'], ['orange', 'red', 'green'], ['blue'], ['orange', 'blue'], ['red', 'blue'], ['orange', 'red', 'blue'], ['green', 'blue'], ['orange', 'green', 'blue'], ['red', 'green', 'blue'], ['orange', 'red', 'green', 'blue']])

if __name__ == '__main__':
    unittest.main()