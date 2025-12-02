def square_Sum(n):  
    if not isinstance(n, int) or n <= 0:
        return 0

    def odd_generator():
        num = 1
        while True:
            yield num
            num += 2

    odd_nums = odd_generator()
    sum_of_squares = sum(next(odd_nums) ** 2 for _ in range(n))

    return sum_of_squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()