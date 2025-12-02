from typing import List

def perfect_squares(a: (int, float), b: (int, float)) -> List[int]:
    result = []
    i = 1
    while i*i <= b:
        if i*i >= a:
            result.append(i*i)
        i += 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()