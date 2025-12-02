# Function to check if a number is odd
def isOdd(num):
    """
    Function to check if a number is odd
    Args:
        num (int): The number to be checked
    Returns:
        bool: True if the number is odd, False otherwise
    """
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    return num % 2 != 0

# Function to get the first digit of a number
def getFirstDigit(num):
    """
    Function to get the first digit of a number
    Args:
        num (int): The number from which the first digit is to be obtained
    Returns:
        int: The first digit of the input number
    """
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    while num >= 10:
        num //= 10
    return num

# Function to get the last digit of a number
def getLastDigit(num):
    """
    Function to get the last digit of a number
    Args:
        num (int): The number from which the last digit is to be obtained
    Returns:
        int: The last digit of the input number
    """
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    return num % 10

# Function to filter an array of numbers based on the given conditions
def specialFilter(nums):
    """
    Function to filter an array of numbers based on the given conditions
    Args:
        nums (list): The list of numbers to be filtered
    Returns:
        int: The count of numbers that meet the filtering conditions
    """
    if not isinstance(nums, list):
        raise ValueError("Input must be a list")
    count = 0
    for num in nums:
        if num > 10 and isOdd(getFirstDigit(num)) and isOdd(getLastDigit(num)):
            count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test2(self):
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()