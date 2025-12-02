def below_threshold(l: list, t: int):
    return all(num < t for num in l) if l else False
import unittest

class Test(unittest.TestCase):
    def test_below_threshold(self):
        self.assertEqual(below_threshold([1, 2, 4, 10], 100), True)
        self.assertEqual(below_threshold([1, 20, 4, 10], 5), False)

if __name__ == '__main__':
    unittest.main()