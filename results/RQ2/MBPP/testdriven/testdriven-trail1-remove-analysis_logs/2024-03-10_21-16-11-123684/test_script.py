def max_val(listval):
    max_value = None
    if isinstance(listval, list) and len(listval) > 0:
        for element in listval:
            if isinstance(element, (int, float)) and (max_value is None or element > max_value):
                max_value = element
        if max_value is not None:
            return max_value
        else:
            return "Error: No numeric values found in the list"
    else:
        return "Error: Empty list or input is not a list"

# Test cases
print(max_val([1, 2, 3, 4, 5]))  # Expected output: 5
print(max_val(['Python', 3, 2, 4, 5, 'version']))  # Expected output: 5
print(max_val([]))  # Expected output: Error: Empty list
print(max_val([-1, -2, -3, -4, -5]))  # Expected output: -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()