def extract_even(test_tuple, even_fnc):
    result = []
    stack = [test_tuple]
    while stack:
        current = stack.pop()
        if isinstance(current, tuple):
            stack.extend(current)
        else:
            if isinstance(current, int) and even_fnc(current):
                result.append(current)
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test_even_ele(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), lambda x: len(x) % 2 == 0), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()