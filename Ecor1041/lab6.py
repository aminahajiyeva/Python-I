# ECOR 1041 Lab 6

__author__ = "Amina Hajiyeva"
__student_number__ = "101303729"

# ======================================================
# Exercise 1

# Type your function definition for Exercise 1 here.

def parrot_trouble(talking: bool, hour: int) -> bool:
    """
    Return True if the parrot is talking outside the allowed times, and we are in trouble.
    Outside times include before 7:00 or after 20:00
    Precondition: hour <= 23 and hour >= 0
    >>> parrot_trouble(False, 23)
    False
    >>> parrot_trouble(True, 3)
    True
    >>> parrot_trouble(True, 10)
    False
    """
    return talking and (hour < 7 or hour > 20)

# ======================================================
# Exercise 2

# Type your function definition for Exercise 2 here.

def alarm_clock(day: int, vacation: bool) -> str:
    """
    Return a string representing the time the alarm will ring. On weekdays the alarm will ring at 7:00, on weekends the alarm will ring at 10:00 however if we are on vacation the alarm will be off.
    Precondition: day <= 6 and day >= 0
    >>> alaram_clock(3, True)
    "off"
    >>> alaram_clock(0, False)
    "10:00"
    >>> alaram_clock(3, False)
    "7:00"
    """

    if not vacation and day != 6 and day != 0:
            return "7:00"
    elif not vacation or vacation and day != 6 and day != 0:
            return "10:00"
    else:
        return "off"

# ======================================================
# Exercise 3

# Type your function definition for Exercise 3 here.

def close_far(a: int, b: int, c: int) -> bool:
    """
    Return True if b or c are close to a (between -1 and +1), while the other value, (b or c) is far from both a and the other value (further than -2 or +2). 
    Precondition: N/A
    >>> close_far(1, 2, 10)
    True
    >>> close_far(1, 2, 3)
    False
    >>> close_far(4, 1, 3)
    True
    """

    if abs(a - b) <= 1 and abs(b - c) >= 2 and abs(c - a) >= 2:
        return True
    elif abs(a - c) <= 1 and abs(c - b) >= 2 and abs(a - b) >= 2:
        return True
    elif abs(b - c) <= 1 and abs(c - a) >= 2 and abs(b - a) >= 2:
        return True
    elif abs(b - a) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2:
        return True
    else:
        return False

    
    
# ======================================================
# Exercise 4

# Type your function definition for Exercise 4 here.

def blackjack(a: int, b: int) -> int:
    """
    Return the integer closest to 21 (without being greater than 21), given two integers. However, if both values are greater than 21, return 0.
    Precondition: a >= 0 and b >= 0.
    >>> blackjack(19, 20)
    20
    >>> blackjack(15, 21)
    21
    >>> blackjack(17, 22)
    17
    >>> blackjack(24, 22)
    0
    """
    if a > 21 and b > 21:
        return 0
    elif a > b:
        if a <= 21:
            return a
        else:
            return b
    elif b > a:
        if b <= 21:
            return b
        else:
            return a
    elif a == b and a <= 21 and b <= 21:
        return a
    else:
        return 0
# ======================================================
# Exercise 5

# Type your function definition for Exercise 5 here.

def assistance(income: float, children: int) -> int:
    """
    Return the amount of money the organization will provide to a family depending on their income, and number of children. With an income of $30k - $40k and 3+ children the assistance is $1.5k per child. With an income of $20k - $30k and 2+ children, the assistance is $1k per child. With an income of less than $20k, the assistance is $2k per child.
    Precondition: children >= 0 and income >= 0.
    >>> assistance(35000, 6)
    9000
    >>> assistance(5000, 3)
    6000
    >>> assistance(22000, 2)
    2000
    """
    if income < 20000:
        return 2000 * children
    elif income >= 20000 and income < 30000 and children >= 2:
        return 1000 * children
    elif income >= 30000 and income < 40000 and children >= 3:
        return 1500 * children
    else:
        return 0

# ======================================================
# Exercise 6

# Type your function definition for Exercise 6 here.

def add_up(n: int) -> float:
    """
    Return the floating number which contains the total series of the given equation
    Precondition: n >= 0.
    >>> add_up(5)
    8.7
    >>> add_up(252)
    1293.48
    >>> add_up(1)
    1.0
    """

    sum = 0
    numerator = 1
    
    while(n >= 1):

        sum += numerator / n
        numerator += 1
        n -= 1
    
    return sum

# ======================================================
# Exercise 7

# Type your function definition for Exercise 7 here.

def fib(n: int) -> int:
    """
    Return the n'th number of the fibonacci sequence
    Precondition: n >= 1
    >>> fib(1)
    1
    >>> fib(6)
    8
    >>> fib(8)
    21
    """

    if n <= 1:
        return 1
    else:
        n1, n2 = 0, 1
        count = 1        
    
        while count < n:
            count += 1
            new = n1 + n2
            n1 = n2
            n2 = new
            
    return new

# ======================================================
# Exercise 8

# Type your function definition for Exercise 8 here.

def years_to_double(initial: float, rate: float) -> int:
    """
    Return the number of years that is required to double the initial investment considering a given interest rate.
    Precondition: initial >=0 and rate >= 0.
    >>> years_to_double(10000, 5.0)
    15
    >>> years_to_double(1500, 7.0)
    11
    >>> years_to_double(10, 1.0)
    70
    """
    years = 0
    total = initial

    while total < (initial * 2):
        years += 1
        annual = initial * pow(1 + (rate / 100), years)
        interest = annual - initial
        total = interest + initial

    return years