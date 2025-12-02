def second_smallest(numbers):
    try:
        if len(numbers) == 0:
            raise ValueError("Error: Input list is empty")
        elif len(numbers) < 2:
            raise ValueError("Error: Input list should have at least two elements")
        
        sorted_numbers = sorted(numbers)
        return sorted_numbers[1]
    
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()