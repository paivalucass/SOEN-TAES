def eat(number, need, remaining):
    if remaining >= need:
        total_eaten = number + need
        remaining -= need
    else:
        total_eaten = number + remaining
        remaining = 0
    return [total_eaten, remaining]
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test2(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test3(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test4(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()