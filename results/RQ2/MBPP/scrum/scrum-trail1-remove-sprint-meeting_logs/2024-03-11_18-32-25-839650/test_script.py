def dog_age(h_age):
    '''Write a function to calculate a dog's age in dog's years.'''
    return h_age * 5
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()