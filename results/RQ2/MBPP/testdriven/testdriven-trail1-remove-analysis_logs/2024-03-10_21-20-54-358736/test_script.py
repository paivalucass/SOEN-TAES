def Find_Min(lst: list[list[int]]) -> list[int]:
    if not lst:
        return []
    min_length = float('inf')
    min_sublist = []
    for sub in lst:
        if len(sub) < min_length:
            min_length = len(sub)
            min_sublist = sub
    return min_sublist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min([[1],[1,2],[1,2,3]]), [1])

if __name__ == '__main__':
    unittest.main()