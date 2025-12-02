def multiple_to_single(L):
    try:
        result = int(''.join(map(str, L)))
        return result
    except (ValueError, TypeError):
        return "Invalid input"

# Testing the function
print(multiple_to_single([11, 33, 50]))  # Output: 113350
print(multiple_to_single([]))  # Output: Invalid input
print(multiple_to_single([5]))  # Output: 5
print(multiple_to_single([11, 'abc', 50]))  # Output: Invalid input
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()