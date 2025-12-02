def eat(number, need, remaining):
    if number < 0 or need < 0 or remaining < 0 or number > 1000 or need > 1000 or remaining > 1000:
        return ["Invalid input"]
    total_eaten_carrots = number + need
    if remaining >= need:
        remaining -= need
    else:
        total_eaten_carrots += remaining
        remaining = 0
    return [total_eaten_carrots, remaining]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])
        self.assertEqual(eat(4, 8, 9), [12, 1])
        self.assertEqual(eat(1, 10, 10), [11, 0])
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()