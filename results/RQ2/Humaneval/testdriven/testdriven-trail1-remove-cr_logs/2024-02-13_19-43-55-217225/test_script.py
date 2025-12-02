def count_seven(num: int) -> int:
    count = 0
    if num < 0:
        num = -num
    while num > 0:
        if num % 10 == 7:
            count += 1
        num //= 10
    return count

def is_divisible_by_11_or_13(num: int) -> bool:
    if num == 0:
        return False
    return num % 11 == 0 or num % 13 == 0

def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(1, n):
        if is_divisible_by_11_or_13(i):
            count += count_seven(i)
    return count
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_3(self):
        self.assertEqual(fizz_buzz(79), 3)

if __name__ == '__main__':
    unittest.main()