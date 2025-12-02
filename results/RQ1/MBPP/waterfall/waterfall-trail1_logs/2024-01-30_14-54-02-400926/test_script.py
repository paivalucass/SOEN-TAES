def Split(numbers: list[int]) -> list[int]:
    if not isinstance(numbers, list):
        raise TypeError("Input parameter 'numbers' should be a list")

    if len(numbers) == 0:
        raise ValueError("Input list is empty")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("Input list contains non-numeric values")

    even_numbers_list = [num for num in numbers if num % 2 == 0]

    return even_numbers_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5]), [2,4])

if __name__ == '__main__':
    unittest.main()