def Strongest_Extension(class_name, extensions):
    strongest_extension = ""
    max_strength = float('-inf')
    
    for ext in extensions:
        uppercase_count = sum(1 for char in ext if char.isupper())
        lowercase_count = sum(1 for char in ext if char.islower())
        strength = uppercase_count - lowercase_count
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = ext
    
    return f"{class_name}.{strongest_extension}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()