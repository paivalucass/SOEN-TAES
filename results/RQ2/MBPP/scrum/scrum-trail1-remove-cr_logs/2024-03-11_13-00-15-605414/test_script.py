def dog_age(h_age):
    '''Write a function to calculate a dog's age in dog's years.'''
    if h_age <= 2:
        return h_age * 10.5
    else:
        return 21 + (h_age - 2) * 4
import unittest

class Test(unittest.TestCase):
    def test_dog_age(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()