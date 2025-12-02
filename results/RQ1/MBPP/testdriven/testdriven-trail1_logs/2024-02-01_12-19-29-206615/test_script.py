def count_X(tup, x):
    '''Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.'''
    try:
        if not isinstance(tup, tuple):
            raise TypeError("Invalid input: Please provide a valid tuple")
        count = tup.count(x)
        return count
    except TypeError as e:
        return str(e)
    except AttributeError as e:
        return "Invalid input: Please provide a valid tuple"
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4), 0)

if __name__ == '__main__':
    unittest.main()