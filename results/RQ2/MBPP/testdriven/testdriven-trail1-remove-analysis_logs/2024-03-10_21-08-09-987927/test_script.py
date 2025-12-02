def smallest_num(xs):
    if not isinstance(xs, list) or not all(isinstance(x, (int, float)) for x in xs):
        return "Invalid input"
    if not xs:
        return None
    return min(xs)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()