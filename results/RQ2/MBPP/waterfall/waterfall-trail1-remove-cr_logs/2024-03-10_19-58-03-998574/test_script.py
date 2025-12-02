def combinations_colors(l, n):
    result = []
    if not isinstance(l, list):
        return "Error: Invalid input for parameter1"
    if n <= 0:
        return result
    for i in range(len(l) ** n):
        temp = []
        for j in range(n):
            temp.append(l[i // (len(l) ** (n - j - 1)) % len(l)])
        result.append(tuple(temp))
    return result
import unittest

class Test(unittest.TestCase):
    def test_combinations_colors(self):
        self.assertEqual(combinations_colors(["Red", "Green", "Blue"], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()