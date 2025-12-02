def planets_between(planet1, planet2):
    planets = {
        "Mercury": 1,
        "Venus": 2,
        "Earth": 3,
        "Mars": 4,
        "Jupiter": 5,
        "Saturn": 6,
        "Uranus": 7,
        "Neptune": 8
    }

    if planet1 not in planets or planet2 not in planets:
        return ()

    index1 = planets[planet1]
    index2 = planets[planet2]

    if index1 < index2:
        result = [planet for planet, index in planets.items() if index > index1 and index < index2]
        return tuple(sorted(result, key=lambda x: planets[x]))
    else:
        result = [planet for planet, index in planets.items() if index > index2 and index < index1]
        return tuple(sorted(result, key=lambda x: planets[x]))
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(function_under_test('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))
    
    def test2(self):
        self.assertEqual(function_under_test('Earth', 'Mercury'), ('Venus'))
    
    def test3(self):
        self.assertEqual(function_under_test('Mercury', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

if __name__ == '__main__':
    unittest.main()