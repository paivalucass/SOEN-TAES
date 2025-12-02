def sort_counter(dict1):
    '''Function to sort a dictionary by value.'''
    sorted_values = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    return sorted_values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}), [('Chemistry', 87), ('Physics', 83), ('Math', 81)])

if __name__ == '__main__':
    unittest.main()