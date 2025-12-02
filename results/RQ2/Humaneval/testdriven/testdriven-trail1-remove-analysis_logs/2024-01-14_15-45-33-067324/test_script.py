from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescales the given list of numbers to fit within the range of 0 to 1 using linear transformation.
    
    Args:
    numbers: List of at least two float numbers
    
    Returns:
    List of float numbers rescaled to the range of 0 to 1
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_number = min(numbers)
    max_number = max(numbers)
    difference = max_number - min_number

    if difference == 0:
        return [0.0] * len(numbers)

    return [(x - min_number) / difference for x in numbers]
  
# Test cases
def test_rescale_to_unit():
    # Test case for list with negative numbers
    assert rescale_to_unit([-1.0, -2.0, -3.0, -4.0, -5.0]) == [1.0, 0.75, 0.5, 0.25, 0.0]

    # Test case for list with only one element
    assert rescale_to_unit([1.0]) == [0.0]

    # Test case for empty list
    assert rescale_to_unit([]) == []
  
    # Test case for list with positive numbers
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
import unittest

class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

if __name__ == '__main__':
    unittest.main()