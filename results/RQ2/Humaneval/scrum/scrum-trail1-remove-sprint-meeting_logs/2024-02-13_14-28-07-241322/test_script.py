def Strongest_Extension(class_name, extensions):
    def calculate_strength(extension):
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        return CAP - SM
    
    if not isinstance(class_name, str) or not isinstance(extensions, list):
        raise TypeError("Invalid input type. Expected string for class_name and list for extensions.")
    
    if not class_name:
        raise ValueError("Invalid input: empty class name")
    
    if not extensions:
        raise ValueError("Invalid input: empty extensions list")
    
    strongest_extension = extensions[0]
    strongest_strength = calculate_strength(extensions[0])
    
    for extension in extensions[1:]:
        strength = calculate_strength(extension)
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    
    return f"{class_name}.{strongest_extension}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'Slices.SErviNGSliCes')
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()