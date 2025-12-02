def Strongest_Extension(class_name, extensions):
    if not class_name:
        return "Error: Empty class name"
    if not extensions:
        return "Error: Empty list of extensions"
    
    def calculate_strength(extension):
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        return cap_count - sm_count
    
    max_strength = float('-inf')
    strongest_extension = ''
    
    for ext in extensions:
        strength = calculate_strength(ext)
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