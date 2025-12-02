def unique_digits(x):
    def has_even_digit(num):
        return any(int(digit) % 2 == 0 for digit in str(num))

    result = [num for num in x if not has_even_digit(num)]
    return sorted(result)

print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()