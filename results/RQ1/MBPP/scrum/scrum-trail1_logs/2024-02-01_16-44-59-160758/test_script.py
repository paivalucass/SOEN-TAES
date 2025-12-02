def second_smallest(numbers):
    if len(numbers) < 2:
        return "List must contain at least 2 numbers"
    
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    return second_smallest

assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()