def round_and_sum(list1):
    def round_numbers(numbers):
        return [round(num) for num in numbers]

    def calculate_total_sum(numbers):
        return sum(numbers)

    def calculate_result(total_sum, length):
        return total_sum * length

    if not list1 or not all(isinstance(num, (int, float)) for num in list1):
        raise ValueError("Input list is empty or contains non-numeric values")

    rounded_list = round_numbers(list1)
    total_sum = calculate_total_sum(rounded_list)
    result = calculate_result(total_sum, len(list1))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()