def sort_counter(dict1):
    if not isinstance(dict1, dict):
        raise TypeError("Input is not a dictionary")

    if not dict1:
        return []

    if not all(isinstance(value, int) for value in dict1.values()):
        raise ValueError("Dictionary values are not all integers")

    sorted_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}), [('Chemistry', 87), ('Physics', 83), ('Math', 81)])

if __name__ == '__main__':
    unittest.main()