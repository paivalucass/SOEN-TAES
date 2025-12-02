def Strongest_Extension(class_name, extensions):
    if not isinstance(class_name, str) or not all(isinstance(ext, str) for ext in extensions):
        raise ValueError("class_name must be a string and extensions must be a list of strings")
    
    if not extensions:
        return ''
    
    strongest_ext = ''
    strongest_strength = float('-inf')
    
    for ext in extensions:
        cap = sum(1 for letter in ext if letter.isupper())
        sm = sum(1 for letter in ext if letter.islower())
        strength = cap - sm
        
        if strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    
    return f"{class_name}.{strongest_ext}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()