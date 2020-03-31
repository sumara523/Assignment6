#Assuming User inputs a valid shape(i.e r, s, c not case sensitive) and valid inputs for length  ,width, and radius i.e positive integers
#Ran Tests using hardcoded inputs
import os
import math

class Shapes:
    def calcStuff(shape,length = 0, width = 0):
        # os.system('clear')
        i = shape.upper()
        # os.system('clear')
        stringReturned = 'Area: '

        if(i == 'R'):
            area = length * width
            perimeter = (2 * length) + (2 * width)
            stringReturned += str(area) +" square units and Perimeter: " + str(perimeter) + " units"
            return stringReturned
        elif(i == "S"):
            area = length * length
            perimeter = 4 * length
            stringReturned += str(area) +" square units and Perimeter: " + str(perimeter) + " units"
            return stringReturned
        else:
            radius = length
            radiusSquared = radius * radius
            area = round(math.pi * radiusSquared,2)
            circumference = round(2 * math.pi * radius, 2)
            stringReturned += str(area) +" square units and Circumference: " + str(circumference) + " units"
            return stringReturned
