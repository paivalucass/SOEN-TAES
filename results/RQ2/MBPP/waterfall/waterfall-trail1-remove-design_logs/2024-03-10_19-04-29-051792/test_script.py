def subject_marks(subjectmarks):
    if not isinstance(subjectmarks, list):
        raise ValueError("Input is not in the expected format")
    
    return sorted(subjectmarks, key=lambda mark: mark[1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()