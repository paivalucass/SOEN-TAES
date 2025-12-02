def round_and_sum(numbersList):
    def is_numeric(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    if all(is_numeric(num) for num in numbersList):
        rounded_numbers = [round(num) for num in numbersList]
        total_sum = sum(rounded_numbers)
        result = total_sum * len(numbersList)
        return result
    else:
        raise ValueError("Input list must contain only numeric values")

# Test cases
print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])) # Output: 243
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()