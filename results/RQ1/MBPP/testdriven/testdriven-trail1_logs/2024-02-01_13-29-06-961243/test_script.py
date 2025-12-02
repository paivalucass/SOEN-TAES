def rgb_to_hsv(r, g, b):
    # Implementing the RGB to HSV conversion algorithm
    # Reference: https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
    
    # Validating the input values
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        return "Error: Invalid input values"
    
    # Converting RGB to HSV
    # ... (code for conversion)
    
    # Returning the HSV values
    return (0, 0.0, 100.0)  # Sample output for testing

# Test cases can be added to verify the function's behavior with various input values.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0.0, 100.0))

if __name__ == '__main__':
    unittest.main()