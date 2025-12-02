def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25,55,65), 55.0)

if __name__ == '__main__':
    unittest.main()