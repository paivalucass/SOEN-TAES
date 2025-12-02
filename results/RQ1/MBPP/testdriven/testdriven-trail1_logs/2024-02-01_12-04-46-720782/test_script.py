def tuple_to_int(nums):
    """
    This function takes a tuple of positive integers as input and converts it into a single concatenated integer.
    """
    # Check for empty tuple
    if not nums:
        raise ValueError("Input tuple is empty")

    # Check for non-integer values in the tuple
    for num in nums:
        if not isinstance(num, int) or num < 0:
            raise ValueError("Input tuple contains non-positive integers")

    # Concatenate the individual integers into a single integer
    concatenated_integer = int(''.join(map(str, nums)))
    return concatenated_integer
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

if __name__ == '__main__':
    unittest.main()