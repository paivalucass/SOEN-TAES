def sum_div(number):
    sum = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            sum += i
            if i != number // i:
                sum += number // i
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()