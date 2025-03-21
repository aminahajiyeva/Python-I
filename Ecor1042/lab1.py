# ECOR 1041 - Bonus

__author__ = "Amina Hajiyeva"
__student_number__ = "101303729"

# ======================================================
# Exercise 1

# Type your function definition for Exercise 1 here.

def replicate(given: str) -> str:
    """
    Return a new string with a number of copies of the original string, depending on the number of characters.
    Precondition: given >= 1.
    >>> replicate("a")
    'a'
    >>> replicate("abc")
    'abcabcabc'
    >>> replicate("hi")
    'hihi'
    """
    total = ""
    
    for i in range(0, len(given)):
        total += given

    return total

# ======================================================
# Exercise 2

# Type your function definition for Exercise 2 here.

def repeat_separator(word: str, sep: str, n: int) -> str:
    """
    Return a new string with a number of copies of the original string depending on the number of characters however, each copy is seperated by an alternate string.
    Precondition: n >= 0.
    >>> repeat_separator("Word", "X", 3)
    'WordXWordXWord'
    >>> repeat_separator("This", "And", 2)
    'ThisAndThis'
    >>> repeat_separator("This", "And", 1)
    'This'
    """
    
    total = ""

    for i in range(0, n):
        if i != n - 1:
            total += word + sep
        else:
            total += word

    return total

# ======================================================
# Exercise 3

# Type your function definition for Exercise 3 here.

def has_pair(s: str, ch: str) -> bool:
    """
    Return True if s contains ch twice next to each other
    Precondition: len(s) >= 2 and len(ch) == 1.
    >>> has_pair('abccd', 'c')
    True
    >>> has_pair('abcdc', 'c')
    False
    >>> has_pair('abcd', 'c')
    False
    """
    if_pair = False
    i = 0

    while i < len(s) - 1:

        if s[i] == ch and s[i + 1] == ch and i != len(s):
            return True
        i += 1
            
    return if_pair




# ======================================================
# Exercise 4

# Type your function definition for Exercise 4 here.
        
def middle_way(list1: list[int], list2: list[int]) -> list[int]:
    """
    Return a new list containing the middle element of the two given lists
    Precondition: len(list1) == 3 and len(list2) == 3.
    >>> middle_way([1,2,3], [4,5,6])
    [2, 5]
    >>> middle_way([7,8,9], [1,2,3])
    [8, 2]
    >>> middle_way([4,5,6], [7,8,9])
    [5, 8]
    """
    new_list = ([list1[1], list2[1]])

    return new_list
    
# ======================================================
# Exercise 5

# Type your function definition for Exercise 5 here.

def make_ends(given_list: list[int]) -> list[int]:
    """
    Return the first and last elements of a given list in a new list
    Precondition: len(given_list) >= 0.
    >>> make_ends([4, 5, 6, 7])
    [4, 7]
    >>> make_ends([1, 2, 3, 4])
    [1, 4]
    >>> make_ends([8, 9, 1, 2])
    [8, 2]
    """
    new_list = ([given_list[0], given_list[-1]])
    
    return new_list

# ======================================================
# Exercise 6

# Type your function definition for Exercise 6 here.

def common_end(list1: list[int], list2: list[int]) -> bool:
    """
    Return True if both given lists have the same first or last element or if both the first and last elements are the same.
    Precondition: len(list1) >= 0 and len(list2) >= 0.
    >>> common_end([1, 2, 3], [4, 5, 6, 7])
    False
    >>> common_end([1, 2, 3], [1, 2, 3, 4, 5, 3])
    True
    >>> common_end([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
    True
    """
    if list1[0] == list2[0] or list1[-1] == list2[-1] or (list1[0] == list2[0] and list1[-1] == list2[-1]):
        return True
    else:
        return False

# ======================================================
# Exercise 7

# Type your function definition for Exercise 7 here.

def count_evens(given_list: list[int]) -> int:
    """
    Return the number of even values in the given list
    Precondition: N/A
    >>> count_evens([1, 2, 3, 4, 5, 6, 7, 8, 9])
    4
    >>> count_evens([10, 11, 12, 13])
    2
    >>> count_evens([1, 3, 5, 7])
    0
    """
    total_evens = 0
    i = 0
    
    while i < len(given_list):
        
        if((given_list[i] % 2) == 0):
            total_evens += 1
        i += 1
            
    return total_evens

# ======================================================
# Exercise 8

# Type your function definition for Exercise 8 here.
def big_diff(given_list: list[int]) -> int:
    """
    Return the difference between the largest and smallest element in the given list
    Precondition: len(given_list) >= 2.
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([1, 2, 3, 4, 5, 6, 7, 8, 9])
    8
    >>> big_diff([100, 40, 43, 823, 764])
    783
    """
    smallest = given_list[0]
    biggest = given_list[0]

    for i in range(0, len(given_list)):
        if given_list[i] < smallest:
            smallest = given_list[i]
        elif given_list[i] >= biggest:
            biggest = given_list[i]

    return biggest - smallest

# ======================================================
# Exercise 9

# Type your function definition for Exercise 9 here.

def has22(given_list: list[int]) -> bool:
    """
    Return True if the given list contains a 2 next to a 2
    Precondition: N/A
    >>> has22([1, 2, 2, 3])
    True
    >>> has22([4, 2, 3, 2])
    False
    >>> has22([22, 3, 5])
    False
    """
    contains22 = True
    for i in range(0, len(given_list)):

        if given_list[i] == 2 and i == len(given_list) - 1:
            return False
        elif given_list[i] == 2 and given_list[i + 1] == 2:
            return True
        else:
            contains22 = False
    return contains22

# ======================================================
# Exercise 10

# Type your function definition for Exercise 10 here.

def centered_average(given_list: list[int]) -> float:
    """
    Return the centered average of the given list - the average of the list ignoring the single largest and single smallest values
    Precondition: len(given_list) >= 3.
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 2, 3, 4, 5, 6, 7, 8, 9])
    5.0
    >>> centered_average([232, 532, 1234, 856, 543])
    643.7
    """

    total_sum = 0

    max_value = max(given_list)
    min_value = min(given_list)

    for i in range(0, len(given_list)):
        total_sum += given_list[i]

    return (total_sum - max_value - min_value) / (len(given_list) - 2)

# ======================================================
# Exercise 11

# Type your function definition for Exercise 11 here.

def bank_statement(given_list: list[float]) -> list[float]:
    """
    Return a new list which contains the sum of deposits, sum of withdrawals, and current account balance, respectively. 
    Precondition: len(given_list) >= 1.
    >>> bank_statement([-4312, 52345, 685, 867, 43, -345])
    [53940, -4657, 49283]
    >>> bank_statement([32.54432, 6543.6354, -543234.23, -523.2345])
    [6576.18, -543757.46, -537181.29]
    >>> bank_statement([234, 6543, 123])
    [6900, 0, 6900]
    """
    deposit = 0
    withdrawals = 0
    current_balance = 0
    i = 0
    
    while i < len(given_list):
        
        if given_list[i] > 0:
            deposit += given_list[i]
        elif given_list[i] < 0:
            withdrawals += given_list[i]
        else:
            current_balance += 0
        i += 1

    current_balance = deposit + withdrawals
    
    new_balance = ([round(deposit, 2), round(
        withdrawals, 2), round(current_balance, 2)])

    return new_balance

# =====================================================
# Exercise 12
# Type your function definition for Exercise 12 here.

def reverse(given_list: list[int]) -> list[int]:
    """
    Return the given list in reverse order
    Precondition: N/A
    >>> reverse([4, 2, 3, 2])
    [2, 3, 2, 4]
    >>> reverse([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> reverse([6, 3, 7, 2, 64])
    64, 2, 7, 3, 6
    """

    reversed_list = []
    for i in given_list:
        reversed_list = [i] + reversed_list

    return reversed_list