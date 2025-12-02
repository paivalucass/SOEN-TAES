def subject_marks(subjectmarks):
    if not isinstance(subjectmarks, list) or not all(isinstance(item, tuple) and len(item) == 2 and isinstance(item[1], (int, float)) for item in subjectmarks):
        raise ValueError("Input must be a list of tuples with exactly two elements where the second element is a valid number")
    
    sorted_list = sorted(subjectmarks, key=lambda x: x[1])
    
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()