def subject_marks(subjectmarks):
    if not all(isinstance(item, tuple) for item in subjectmarks):
        raise ValueError("Subjectmarks should be a list of tuples")
    
    sorted_list = sorted(subjectmarks, key=lambda x: x[1], reverse=False)
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), 
                         [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()