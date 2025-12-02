def combinations_list(list1):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(list1)):
            path.append(list1[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_list(['orange', 'red', 'green', 'blue']), [[], ['orange'], ['red'], ['orange', 'red'], ['green'], ['orange', 'green'], ['red', 'green'], ['orange', 'red', 'green'], ['blue'], ['orange', 'blue'], ['red', 'blue'], ['orange', 'red', 'blue'], ['green', 'blue'], ['orange', 'green', 'blue'], ['red', 'green', 'blue'], ['orange', 'red', 'green', 'blue']])

if __name__ == '__main__':
    unittest.main()