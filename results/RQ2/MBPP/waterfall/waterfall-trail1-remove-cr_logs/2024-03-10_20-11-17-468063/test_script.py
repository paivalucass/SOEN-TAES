def armstrong_number(number):
    num_str = str(number)
    num_length = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_length
    return sum == number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()