def checkBalance(q):
    return q == q[::-1]

def calculateSum(q):
    return sum(q)

def checkMaxWeight(q, w):
    return calculateSum(q) <= w

def will_it_fly(q, w):
    return checkBalance(q) and checkMaxWeight(q, w)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)
        self.assertEqual(will_it_fly([3], 5), True)

if __name__ == '__main__':
    unittest.main()