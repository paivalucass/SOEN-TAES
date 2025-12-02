def get_pairs_count(arr, sum):
    '''
    Write a python function to count the number of pairs whose sum is equal to ‘sum’.
    The function gets as input a list of numbers and the sum.
    '''
    # Check if the input list contains only integers and if the sum is an integer
    if not all(isinstance(x, int) for x in arr) or not isinstance(sum, int):
        raise ValueError("Invalid input. The input list should only contain integers and the sum should be an integer.")
    
    # Create a frequency dictionary to store the count of each number in the input list
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Initialize the pairs count
    pairs_count = 0
    
    # Iterate through the input list to find pairs that sum up to the given sum
    for num in arr:
        complement = sum - num
        if complement in frequency:
            pairs_count += frequency[complement]
        if complement == num:
            pairs_count -= 1
    
    # Each pair is counted twice, so divide by 2 to get the actual count
    return pairs_count // 2  # Returns the count of pairs whose sum is equal to 'sum'

# Test case
assert get_pairs_count([1,1,1,1], 2) == 6  # Verify the correctness of the code with a test case
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()