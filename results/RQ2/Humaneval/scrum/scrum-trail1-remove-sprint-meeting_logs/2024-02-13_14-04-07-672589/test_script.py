def is_multiply_prime(a):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def get_prime_numbers():
        prime_numbers = []
        for num in range(2, 100):
            if is_prime(num):
                prime_numbers.append(num)
        return prime_numbers
    
    if a <= 0 or a > 100:
        return False
    
    prime_numbers = get_prime_numbers()
    count = 0
    for num in prime_numbers:
        if a % num == 0:
            count += 1
    return count == 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)

if __name__ == '__main__':
    unittest.main()