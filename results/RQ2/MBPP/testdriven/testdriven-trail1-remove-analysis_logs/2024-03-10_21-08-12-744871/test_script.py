def subject_marks(subjectmarks):
    '''Write a function to sort a list of tuples using the second value of each tuple.
    assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''
    if not subjectmarks:
        raise ValueError("Input list is empty")
    for subjectmark in subjectmarks:
        if not isinstance(subjectmark, tuple) or len(subjectmark) != 2 or not isinstance(subjectmark[1], int):
            raise ValueError("Input list contains invalid data")
    return sorted(subjectmarks, key=lambda x: x[1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()