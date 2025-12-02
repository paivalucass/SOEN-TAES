def eat(number, need, remaining):
    if not (0 <= number <= 1000):
        raise ValueError("Invalid input for number parameter. Number of carrots eaten must be between 0 and 1000.")
    if not (0 <= need <= 1000):
        raise ValueError("Invalid input for need parameter. Number of carrots needed must be between 0 and 1000.")
    if not (0 <= remaining <= 1000):
        raise ValueError("Invalid input for remaining parameter. Number of remaining carrots must be between 0 and 1000.")

    totalEatenCarrots = number + remaining
    if remaining >= (need - number):
        carrotsLeft = remaining - (need - number)
    else:
        carrotsLeft = 0

    return [totalEatenCarrots, carrotsLeft]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])
        self.assertEqual(eat(4, 8, 9), [12, 1])
        self.assertEqual(eat(1, 10, 10), [11, 0])
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()