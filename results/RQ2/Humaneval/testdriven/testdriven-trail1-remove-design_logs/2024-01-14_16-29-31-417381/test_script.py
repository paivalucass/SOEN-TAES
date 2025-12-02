def eat(number, need, remaining):
    total_eaten = number + need
    if total_eaten <= remaining:
        return [total_eaten, remaining - total_eaten]
    else:
        return [total_eaten, 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])
        self.assertEqual(eat(4, 8, 9), [12, 1])
        self.assertEqual(eat(1, 10, 10), [11, 0])
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()