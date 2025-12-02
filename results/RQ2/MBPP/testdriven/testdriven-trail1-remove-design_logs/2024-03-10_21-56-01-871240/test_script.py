def subject_marks(subjectmarks):
    '''Write a function to sort a list of tuples using the second value of each tuple.'''
    sorted_list = sorted(subjectmarks, key=lambda x: x[1])
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), 
                         [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()