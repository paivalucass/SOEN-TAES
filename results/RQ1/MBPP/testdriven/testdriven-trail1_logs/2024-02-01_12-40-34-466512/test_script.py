def round_numbers(num):
    return round(num)

def calculate_sum(numbers):
    return sum(numbers)

def round_and_sum(number_list):
    '''Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.'''
    try:
        rounded_numbers = [round_numbers(num) for num in number_list]
        total_sum = calculate_sum(rounded_numbers)
        result = total_sum * len(number_list)
        return result
    except (ValueError, TypeError):
        return "Error: Input list contains non-numeric values."
    except ZeroDivisionError:
        return "Error: Input list is empty."
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()