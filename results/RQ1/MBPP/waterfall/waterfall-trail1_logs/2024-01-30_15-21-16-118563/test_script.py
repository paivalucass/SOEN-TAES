def even_ele(test_tuple, even_fnc):
    result = []
    stack = [test_tuple]
    while stack:
        current = stack.pop()
        if isinstance(current, tuple):
            stack.extend(current)
        else:
            if even_fnc(current):
                result.append(current)
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), even_fnc), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()