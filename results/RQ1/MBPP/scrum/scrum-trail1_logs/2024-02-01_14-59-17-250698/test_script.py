def babylonian_squareroot(number):
    # Implement the Babylonian method algorithm for computing square roots
    # Add error handling for invalid input
    # Display the square root value in a visually appealing way
    import math
    if isinstance(number, (int, float)):
        if number < 0:
            return "Error: Invalid input. Please enter a positive number."
        elif number == 0:
            return 0
        else:
            x = number
            y = 1
            e = 0.000001
            while x - y > e:
                x = (x + y) / 2
                y = number / x
            return round(x, 15)
    else:
        return "Error: Invalid input. Please enter a numeric value."
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()