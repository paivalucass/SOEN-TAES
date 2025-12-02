def rgb_to_hsv(r, g, b):
    # Write your code here
    pass

# Suggestions:
# {
#   "Architect": "Consider using built-in functions or libraries for converting RGB to HSV to ensure accuracy and efficiency. Also, consider error handling for invalid input values.",
#   "Tester": "Test the function with a wide range of RGB values to ensure that the conversion to HSV is accurate. Also, test edge cases and invalid input values to ensure proper error handling."
# }

# Original code:
def rgb_to_hsv(r, g, b):
    # Write your code here
    pass

# Rewrite the code here:
import colorsys

def rgb_to_hsv(r, g, b):
    try:
        r_normalized = r / 255.0
        g_normalized = g / 255.0
        b_normalized = b / 255.0
        hsv = colorsys.rgb_to_hsv(r_normalized, g_normalized, b_normalized)
        return (round(hsv[0] * 360), round(hsv[1] * 100, 1), round(hsv[2] * 100, 1))
    except ValueError:
        print("Invalid RGB values")
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0.0, 100.0))

if __name__ == '__main__':
    unittest.main()