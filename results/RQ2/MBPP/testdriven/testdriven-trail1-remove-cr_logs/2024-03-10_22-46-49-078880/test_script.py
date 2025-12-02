def armstrong_number(number):
    num = str(number)
    n = len(num)
    total = 0
    for digit in num:
        total += int(digit) ** n
    return total == number
import unittest

class Test(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()