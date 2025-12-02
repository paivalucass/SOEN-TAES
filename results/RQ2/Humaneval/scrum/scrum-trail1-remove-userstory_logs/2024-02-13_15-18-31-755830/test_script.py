def filter_even_digits(num):
    return all(int(digit) % 2 != 0 for digit in str(num))

def function_under_test(x):
    try:
        # Input validation
        for num in x:
            if not isinstance(num, int) or num < 0:
                raise ValueError("Input list should only contain positive integers")

        # Iteration and filtering
        result = [num for num in x if filter_even_digits(num)]

        # Sorting
        result.sort()

        # Return
        return result

    except Exception as e:
        return str(e)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(function_under_test([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()