def eat(number, need, remaining):
    if number < 0 or need < 0 or remaining < 0:
        return "Invalid input"

    if remaining < need:
        eaten = number + remaining
        remaining = 0
    else:
        eaten = number + need
        remaining -= need

    return [eaten, remaining]
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_2(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test_3(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test_4(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()