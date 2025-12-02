def combinations_list(lst):
    result = []

    for i in range(len(lst) + 1):
        temp = []
        combinations_recursive(lst, i, 0, [], temp)
        result.extend(temp)

    return result

def combinations_recursive(arr, k, start, current, result):
    if k == 0:
        result.append(list(current))
        return
    for i in range(start, len(arr)):
        current.append(arr[i])
        combinations_recursive(arr, k-1, i+1, current, result)
        current.pop()
import unittest

class Test(unittest.TestCase):
    def test_combinations_list(self):
        self.assertEqual(combinations_list(['orange', 'red', 'green', 'blue']), [[], ['orange'], ['red'], ['orange', 'red'], ['green'], ['orange', 'green'], ['red', 'green'], ['orange', 'red', 'green'], ['blue'], ['orange', 'blue'], ['red', 'blue'], ['orange', 'red', 'blue'], ['green', 'blue'], ['orange', 'green', 'blue'], ['red', 'green', 'blue'], ['orange', 'red', 'green', 'blue']])

if __name__ == '__main__':
    unittest.main()