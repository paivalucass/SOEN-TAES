def combinations_colors(l, n):
    if n < 0:
        return "Invalid input length"
    if n == 0:
        return [()]
    result = []
    for i in range(len(l)):
        for next in combinations_colors(l, n-1):
            result.append((l[i],) + next)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_colors( ["Red","Green","Blue"],1),[('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()