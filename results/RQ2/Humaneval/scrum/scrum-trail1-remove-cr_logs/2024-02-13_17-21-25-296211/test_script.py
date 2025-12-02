def Strongest_Extension(class_name, extensions):
    strongest_extension = max(extensions, key=lambda x: sum(1 for c in x if c.isupper()) - sum(1 for c in x if c.islower()))
    return f"{class_name}.{strongest_extension}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()