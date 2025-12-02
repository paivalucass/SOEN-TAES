import math

def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total_sum += math.comb(n, i)
    return total_sum
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()