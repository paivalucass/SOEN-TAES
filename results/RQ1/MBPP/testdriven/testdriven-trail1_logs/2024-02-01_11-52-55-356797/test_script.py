def subject_marks(subjectmarks):
    '''Write a function to sort a list of tuples using the second value of each tuple.'''
    if not isinstance(subjectmarks, list) or not all(isinstance(x, tuple) and len(x) >= 2 for x in subjectmarks):
        raise ValueError("Input is not a list of tuples or tuples have less than 2 elements")
    return sorted(subjectmarks, key=lambda x: x[1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()