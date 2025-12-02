def find_largest_prime(lst):
    max_prime = 0
    for num in lst:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                if num > max_prime:
                    max_prime = num
    return max_prime

def sum_of_digits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

def largest_prime_sum(lst):
    largest_prime = find_largest_prime(lst)
    return sum_of_digits(largest_prime)
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(largest_prime_sum([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)

    def test_2(self):
        self.assertEqual(largest_prime_sum([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)

    def test_3(self):
        self.assertEqual(largest_prime_sum([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)

    def test_4(self):
        self.assertEqual(largest_prime_sum([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)

    def test_5(self):
        self.assertEqual(largest_prime_sum([0,81,12,3,1,21]), 3)

    def test_6(self):
        self.assertEqual(largest_prime_sum([0,8,1,2,1,7]), 7)

if __name__ == '__main__':
    unittest.main()