def unique_digits(x):
    result = []
    for num in x:
        has_even_digit = False
        temp = num
        while temp > 0:
            digit = temp % 10
            if digit % 2 == 0:
                has_even_digit = True
                break
            temp = temp // 10
        if not has_even_digit:
            result.append(num)
    return sorted(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()