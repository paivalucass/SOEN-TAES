def sum_div(number):
    if number <= 0:
        return "Error Message"
    else:
        divisors_sum = 1
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                divisors_sum += i
                if i != number // i:
                    divisors_sum += number // i
        return divisors_sum

assert sum_div(8) == 7
assert sum_div(7) == 8
assert sum_div(-5) == "Error Message"
assert sum_div(0) == "Error Message"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()