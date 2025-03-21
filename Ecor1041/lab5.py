# ECOR 1041 Lab 5

__author__ = "Amina Hajiyeva"
__student_number__ = "101303729"

#======================================================
# Exercise 1

# Type your function definition for Exercise 1 here.
TWENTY_PERCENT_TIP = 0.80
FIFTEEN_PERCENT_TIP = 0.85
FIVE_PERCENT_TIP = 0.95

def tip(cost: float, satisfaction: int) -> float:
    """
    Return the suggested tip amount, calculated by considering the cost of the food as well as the satisfaction level of the service. For level of satisfactory, 1 = totally satisfied, 2 = somewhat satisfied, 3 = dissatisfied.
    Precondition: cost >= 0, satisfaction == 1 or satisfaction == 2 or satisfaction == 3.
    >>> tip(50, 1)
    10.0
    >>> tip(132.45, 2)
    19.87
    >>> tip(34.54, 3)
    1.73
    """

    if satisfaction == 1:
        cost -= cost * TWENTY_PERCENT_TIP
    elif satisfaction == 2:
        cost -= cost * FIFTEEN_PERCENT_TIP
    else:
        cost -= cost * FIVE_PERCENT_TIP
        
    return cost

# ======================================================
# Exercise 2

# Type your function definition for Exercise 2 here.

def coupon(amount_spent_on_groceries: float) -> int:
    """
    Return the value of a coupon that can be applied on purchased groceries, depending on the amount of money spent. If less then $10 is spent, coupon is 0%. If between $10-$60 is spent, coupon is 8%. if between $60-$150 is spent, 10%. If $150-$210 is spent, coupon is 12%. If more than $210 spent, coupon is 14%.
    Precondition: amount_spent_on_groceries >= 0.
    >>> coupon(11)
    0.88
    >>> coupon(65.76)
    6.576
    >>> coupon(476.4)
    66.696
    """

    coupon = amount_spent_on_groceries

    if amount_spent_on_groceries < 10:
        coupon = 0
    elif amount_spent_on_groceries >= 10 and amount_spent_on_groceries <= 60:
        coupon -= amount_spent_on_groceries * 0.92
    elif amount_spent_on_groceries >= 60 and amount_spent_on_groceries <= 150:
        coupon -= amount_spent_on_groceries * 0.90
    elif amount_spent_on_groceries >= 150 and amount_spent_on_groceries <= 210:
        coupon -= amount_spent_on_groceries * 0.88
    else:
        coupon -= amount_spent_on_groceries * 0.86

    return coupon

# ======================================================
# Exercise 3

# Type your function definition for Exercise 3 here.

def bakers_party(weekend: bool, number_of_pastries: int) -> bool:
    """
    Return True or False if the bakers party is succesful or not. If the party has between 40 and 60 pastries (inclusive) on a weekday, then the party is succesful. However, if it is a weekend there is no upper bound on pastries.
    Precondition: number_of_pastries >= 0.
    >>> bakers_party(False, 50)
    True
    >>> bakers_party(True, 80)
    True
    >>> bakers_party(False, 23)
    False
    
    """
    if weekend and number_of_pastries < 40:
        success = False
    elif weekend and number_of_pastries >= 40 and number_of_pastries <= 60:
        success = True
    elif weekend and number_of_pastries > 60:
        success = True
    elif not weekend and number_of_pastries < 40:
        success = False
    elif not weekend and number_of_pastries >= 40 and number_of_pastries <= 60:
        success = True
    else:
        success = False
    return success


# ======================================================
# Exercise 4

# Type your function definition for Exercise 4 here.

def squirrel_play(summer: bool, temperature: int) -> bool:
    """
    Return True if the squirells are playing or False if they are not playing. The squirells play in the summer when the temperature is between 40-100(inclusive). If not summer, they play between the temperatures 40-90(inclusive).
    Precondition: N/A
    >>> squirrel_play(True, 100)
    True
    >>> squirrel_play(False, 100)
    False
    >>> squirrel_play(False, 34)
    False
    """
    if (not summer and temperature >= 60 and temperature <= 90) or (summer and temperature >= 60 and temperature <= 100):
        play = True
    else:
        play = False
    return play

# ======================================================
# Exercise 5

# Type your function definition for Exercise 5 here.

def great_42(a: int, b: int) -> bool:
    """
    Return True if either a or b has a value of 42, or if their sum is 42, or if the absolute value of their difference is 42. Otherwise return False.
    Precondition: N/A
    >>> great_42(21, 21)
    True
    >>> great_42(42, 543)
    True
    >>> great_42(0, 0)
    False
    """

    if (a + b == 42) or (a == 42) or (b == 42) or (abs(a - b) == 42):
        return True
    else:
        return False

# ======================================================
# Exercise 6

# Type your function definition for Exercise 6 here.

def multiply_uniques(a: int, b: int, c: int) -> int:
    """
    Return the product of all the parameters. If one of the values is identical to another, that value is omitted and only the unrelated value is used. Additionally, if all three values are identical, then the value returned is 1.
    Precondition: N/A
    >>> multiply_uniques(15, 34, 15)
    34
    >>> multiply_uniques(2, 3, 6)
    36
    >>> multiply_uniques(12, 12, 12)
    1
    """
    if (a == b) and (b == c):
        return 1
    elif (a == b):
        return c
    elif (a == c):
        return b
    elif (b == c):
        return a
    else:
        return a * b * c