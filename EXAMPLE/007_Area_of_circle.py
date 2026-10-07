
#! Using hardcoded pi value
import numpy as np
import math
PI = 3.142


def area_of_circle(radius):
    return PI * (radius ** 2)


r = float(input('Enter the radius: '))
area = area_of_circle(r)
print(f'Area of circle is: {area}')

#! Using math method:
radius = 5
area = math.pi * (radius ** 2)
print(f'Area of circle is: {area}')

#! Using numpy method:
radius = 5
area = np.pi * pow(radius, 2)
print(f'Area of circle is: {area}')
