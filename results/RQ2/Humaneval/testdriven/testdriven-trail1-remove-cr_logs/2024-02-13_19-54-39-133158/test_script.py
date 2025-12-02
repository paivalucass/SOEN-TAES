def eat(number, need, remaining):
    if not (0 <= number <= 1000) or not (0 <= need <= 1000) or not (0 <= remaining <= 1000):
        return "Invalid input. Please make sure all inputs are within the specified constraints."

    total_eaten = number + need
    if remaining >= total_eaten:
        return [total_eaten, remaining - total_eaten]
    else:
        return [total_eaten, 0]
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