def extract_even(test_tuple, even_fnc):
    result = []
    stack = [test_tuple]
    while stack:
        current = stack.pop()
        temp = []
        for item in current:
            if isinstance(item, tuple):
                stack.append(item)
            else:
                if isinstance(item, int) and even_fnc(item):
                    temp.append(item)
        if temp:
            result.append(tuple(temp))
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()