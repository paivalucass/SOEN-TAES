def dog_age(h_age):
    '''
    Function to calculate a dog's age in dog years.

    Parameters:
    h_age (int): The human age of the dog.

    Returns:
    int: The equivalent age in dog years.
    '''
    if not isinstance(h_age, int) or h_age <= 0:
        raise ValueError("Input must be a positive integer")

    # Calculate the equivalent age in dog years using the following formula: dog_age = h_age * 7
    dog_age = h_age * 5  # Calculate the equivalent age in dog years
    return dog_age
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()