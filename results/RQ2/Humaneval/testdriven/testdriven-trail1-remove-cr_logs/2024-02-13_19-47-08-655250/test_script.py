def is_multiply_prime(a):
    if a < 0:
        return "Error: Non-numeric input"
    elif a == 0 or a == 1:
        return False
    elif a < 100:
        factors = []
        for i in range(2, a):
            if a % i == 0:
                prime = True
                for j in range(2, i):
                    if i % j == 0:
                        prime = False
                        break
                if prime:
                    factors.append(i)
        if len(factors) >= 3:
            return True
        else:
            return False
    else:
        return "Error: Input number is greater than or equal to 100"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)

if __name__ == '__main__':
    unittest.main()