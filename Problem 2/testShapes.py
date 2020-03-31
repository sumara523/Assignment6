#Assuming User inputs a valid shape(i.e r, s, c not case sensitive) and valid inputs for length  ,width, and radius i.e positive integers
#Ran Tests using hardcoded inputs

import unittest
from terminalPractice import Shapes

class TestShapes(unittest.TestCase):
    def testShape(self):
        result = Shapes.calcStuff('R',15,2)
        self.assertEqual(result, 'Area: 30 square units and Perimeter: 34 units')

        result = Shapes.calcStuff('r',20,2)
        self.assertEqual(result, 'Area: 40 square units and Perimeter: 44 units')


        result = Shapes.calcStuff('S',5)
        self.assertEqual(result, 'Area: 25 square units and Perimeter: 20 units')

        result = Shapes.calcStuff('S', 4)
        self.assertEqual(result, 'Area: 16 square units and Perimeter: 16 units')

        result = Shapes.calcStuff('s', 10)
        self.assertEqual(result, 'Area: 100 square units and Perimeter: 40 units')



        result = Shapes.calcStuff('C', 4)
        self.assertEqual(result,"Area: 50.27 square units and Circumference: 25.13 units")

        result = Shapes.calcStuff('c', 10)
        self.assertEqual(result,"Area: 314.16 square units and Circumference: 62.83 units")

if __name__ == '__main__':
    unittest.main()
