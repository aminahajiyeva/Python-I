# ECOR 1041 Lab 4

__author__ = "Amina Hajiyeva"
__student_number__ = "101303729"

import math

# =====================================================
# Exercise 1

# Type your function definition for Exercise 1 here.

def area_of_disk(radius: float) -> float:
    """
    Return the area of a disk with the specified radius.
    Precondition: radius >= 0.
    >>> area_of_disk(5)
    78.54
    >>> area_of_disk(10)
    314.16
    >>> area_of_disk(15)
    706.86
    """
    return math.pi * radius**2
    

# =======================================================
# Exercise 2

# Type your function definition for Exercise 2 here.

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg: float) -> float:
    """
    Return the liters per 100km, given miles per gallon.
    Precondition: mpg >= 0.
    >>>convert_to_litres_per_100_km(32)
    8.83
    >>>convert_to_litres_per_100_km(100)
    2.83
    >>>convert_to_litres_per_100_km(5.3)
    53.30
    """
    return 100 / (mpg * KMS_PER_MILE / LITRES_PER_GALLON)

# =======================================================
# Exercise 3

# Type your function definition for Exercise 3 here.

def accumulated_amount(principal: float, rate: float, n: int, time: int) -> float:
    """
    Return the amount of money after depositing it into a bank, and earning interest.
    Precondition: principal and time <= 0, rate and n < 0.
    >>>accumulated_amount(1500, 0.043, 4, 6)
    1938.84
    >>>accumulated_amount(0, 0.043, 4, 6)
    0
    >>>accumulated_amount(1500, 0, 4, 6)
    1500
    """
    return principal * pow(1 + (rate / n), n * time)

# =======================================================
# Exercise 4

# Type your function definition for Exercise 4 here.

def area_of_cone(height: float, radius: float) -> float:
    """
    Return the lateral surface area of a right circular cone given the height and radius
    Precondition: height and radius < 0.
    >>> area_of_cone(3, 15)
    720.86
    >>> area_of_cone(45, 18)
    2740.72
    >>> area_of_cone(31.5, 72.1)
    17821.88
    """
    return math.pi * radius * math.sqrt(radius**2 + height**2)

# =======================================================
# Exercise 5

# Type your function definitions for Exercise 5 here.

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Return the distance between two points, given two points
    Precondition: 
    >>> distance(1, 1, 4, 5)
    5.0
    >>> distance(7, 3, 9, 1)
    2.83
    >>> distance(5.2, 7.9, 3.6, 1.7)
    6.40
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def area_of_circle(xc: int, yc: int, xp: int, yp: int) -> float:
    """
    Return the area of a circle, given a point in the center & one on the perimeter, using distance() function, and area_of_disk() function.
    Precondition: radius <= 0.
    >>> area_of_circle(4, 3, 3, 7)
    53.41
    >>> area_of_circle(9,3,7,4)
    15.71
    >>> area_of_circle(17.53, 32.64, 54.86, 45.37)
    4887.00
    """
    return area_of_disk(distance(xc, yc, xp, yp))