def planets_between(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    if index1 == index2:
        return ()
    
    start = min(index1, index2)
    end = max(index1, index2)
    
    result = planets[start+1:end]
    
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bf('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))
        self.assertEqual(bf('Earth', 'Mercury'), ('Venus'))
        self.assertEqual(bf('Mercury', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

if __name__ == '__main':
    unittest.main()