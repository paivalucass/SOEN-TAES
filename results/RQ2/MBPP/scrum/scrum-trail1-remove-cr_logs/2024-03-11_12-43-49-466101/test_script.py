def amicable_numbers_sum(limit):
    amicable_sum = 0
    for num in range(1, limit+1):
        if is_amicable(num):
            amicable_sum += num
    return amicable_sum


def is_amicable(num):
    sum_divisors = sum(divisors(num))
    if sum_divisors != num and sum(divisors(sum_divisors)) == num:
        return True
    else:
        return False


def divisors(n):
    divisors_list = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n // i:
                divisors_list.append(n // i)
    return divisors_list

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()