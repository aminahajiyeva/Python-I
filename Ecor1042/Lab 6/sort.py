# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "John Samis, Charlie Tierney, Shoubh Patel, Amina Hajiyeva"

# Update "" with your team (e.g. T102)
__team__ = "T082"

#==========================================#
# Place your sort_cache_bubble function after this line

def sort_cache_bubble(machine_dic_list: list[dict], order_of_list: str) -> list:
    """    
    Return the list of machines given using the bubble sort algorithim in acsending or decsending order - as determined by the user. Additionally, if CACH is not a key within the list of dictionaries, print a message informing the user and return the original list given. 
    
    Precondition: order_of_list == "A" or order_of_list == "D".
    
    >>> sort_cache_bubble([{"CACH":10,"Model":"GP"},{"CACH":19,"Model":"MS"}], "D")
    [{"CACH": 19, "Model":"MS"}, {"CACH":10, "Model":"GP"}]
    
    >>> sort_cache_bubble([{"Model":"GP"}, {"Model":"MS"}], "D")
    "CACH" key is not present.
    [{"Model":"GP"}, {" Model":"MS"}]
    
    >>> sort_cache_bubble([{"CACH":10,"Model":"GP"},{"CACH":19,"Model":"MS"}], "A")
    [{"CACH":10, "Model":"GP"}, {"CACH": 19, "Model":"MS"}]
    
    """
    # since list contains dictionaries, need to iteate through keys and values
    for i in range(len(machine_dic_list) - 1):
        for j in range(0, len(machine_dic_list) - i - 1):
            # determine whether the keys in the dicionaries contain 'CACH'
            if 'CACH' in machine_dic_list[j] and 'CACH' in machine_dic_list[j + 1]:
                # if the dictionaries contain cache and the user wants the output to be in ascending order, make a new variable to store the value as a place holder while swapping and sorting the order
                if (order_of_list.upper() == 'A' and machine_dic_list[j]['CACH'] > machine_dic_list[j + 1]['CACH']):
                    place_holder = machine_dic_list[j]
                    machine_dic_list[j] = machine_dic_list[j + 1]
                    machine_dic_list[j + 1] = place_holder
                # if the dictionaries contain cache and the user wants the output to be in decsending order, make a new variable to store the value as a place holder while swapping and sorting the order
                elif (order_of_list.upper() == 'D' and machine_dic_list[j]['CACH'] < machine_dic_list[j + 1]['CACH']):
                    place_holder = machine_dic_list[j]
                    machine_dic_list[j] = machine_dic_list[j + 1]
                    machine_dic_list[j + 1] = place_holder
            # if the user gives an invalid input, inform them of this by printing out a message and return their original list
            else:
                print("'CACH' key is not present")
                # return machine_dic_list

    # return the sorted
    return machine_dic_list
#==========================================#
# Place your sort_prp_selection function after this line
def sort_prp_selection(list_dict: list[dict], direction: str) -> list:
    """Return list of dictionaries containing 'PRP' sorted in ascending or descending order depending on the user input. If the list does not contain 'PRP', the function will print an error message and return the original list.
    
    Pre conditions: dictionary == 'A' or 'D'
    
    Examples: 
    
    >>>sort_prp_selection ( [{"PRP":10,"Model":"GP"}, {"PRP":19,"Model":"MS"}], "D")
    [{"PRP": 19, "Model":"MS"}, {"PRP":10, "Model":"GP"}]
    >>>sort_prp_selection([{"Model":"GP"},{"Model":"MS"}], "D")
    "PRP" key is not present
    [{"Model":"GP"}, {"Model":"MS"}]
    """ 
    
    for item in list_dict:
        if 'PRP' in item:
    
            if direction == 'A':
                for i in range(len(list_dict)):
                    # Find the minimum element in remaining
                    # unsorted array 
                    min_idx = i
                    for j in range(i+1, len(list_dict)):
                        if list_dict[min_idx]['PRP'] > list_dict[j]['PRP']:
                            min_idx = j
                        
                    list_dict[i], list_dict[min_idx] = list_dict[min_idx], list_dict[i]
    
    
            elif direction == 'D':
                for i in range(len(list_dict)):
                    # Find the minimum element in remaining
                    # unsorted array 
                    min_idx = i
                    for j in range(i+1, len(list_dict)):
                        if list_dict[min_idx]['PRP'] < list_dict[j]['PRP']:
                            min_idx = j
                        
                    list_dict[i], list_dict[min_idx] = list_dict[min_idx], list_dict[i]
    
    
        else: 
            print('"PRP" is not a key in the dictionary')
    return list_dict   

#==========================================#
# Place your sort_m_avg_insertion function after this line

def sort_m_avg_insertion(students: list, sorting_method: str) -> list:

    """

    Return a sorted list containing the dictonaries based off PRP values, returns
    in ascending order if "A" is the argument for sorting_method and returns
    in descending order if "D" is the argument for sorting_method

    >>>sort_m_avg_insertion([{'M_AVG': 15, 'Model': 'Universe'}, {'M_AVG': 22, 'Model': '67'}, 'D')
    [{'M_AVG': 22, 'Model': '67'}, {'M_AVG': 15, 'Model': 'Universe'}]

    >>>sort_m_avg_insertion([{'Vendor': 'amadhal'}, {'ERP': 200}], 'D')
    '"M_AVG" key is not present' [{'Vendor': 'amadhal'}, {'ERP': 200}]

    >>>sort_m_avg_insertion([])
    []
    """
    if students == []:  # Checks for a blank list
        return students  # Returns the blank list

    # Checks if M_AVG is in the dictonary
    if not 'M_AVG' in students[0].keys():
        return students  # If M_AVG isnt in the dictonary returns the list

    elif sorting_method == 'A':  # Ascending order
        for i in range(1, len(students)):
            key = students[i]  # Sets key to the value i in students
            j = i - 1
            # Loop proceeds if M_AVG in dictonary i - 1 is greater then M_AVG in the dictonary associated with i
            while j >= 0 and key.get('M_AVG') < students[j].get('M_AVG'):
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = key
        return students  # Returns a sorted list
    
    elif sorting_method == 'D':  # Descending order
        for i in range(1, len(students)):  # Same code as ascending sort
            key = students[i]
            j = i - 1
            while j >= 0 and key.get('M_AVG') < students[j].get('M_AVG'):
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = key

        # Takes the list and reverses it for descending order
        students.reverse() == students
        return students
#==========================================#
# Place your sort_myct_bubble function after this line

def sort_myct_bubble(dict_list: list[dict], A_or_D: str) -> list:
    """
    Using the bubble sort algorithm, sort the list of machines' dictionaries
    by the 'MYCT' attribute. If 'MYCT' is a key in the dict, return the new sorted list.
    If it is not present in the dict, print a message stating the key is not in 
    the dictionnary and return the original list.

    Preconditions: 
    Assume input parameters are valid.
    Data does not include any duplicate entries.

    Examples:
    >>>sort_myct_bubble([{"MYCT":10,"Model":"GP"},{"MYCT":19,"Model":"MS"}],"D")
    [{"MYCT": 19, "Model":"MS"}, {"MYCT":10, "Model":"GP"}]

    >>>sort_myct_bubble([{"Model":"GP"}, {"Model":"MS"}], "D")
    "MYCT" key is not present.
    [{"Model":"GP"}, {"Model":"MS"}]

    >>>sort_myct_bubble([], 'A')
    []
    """
    for i in range(len(dict_list) - 1):
        if 'MYCT' in dict_list[i]:
            for j in range(0, len(dict_list) - i - 1):
                if A_or_D == 'A':
                    if dict_list[j]['MYCT'] > dict_list[j + 1]['MYCT']:
                        temp = dict_list[j]
                        dict_list[j] = dict_list[j+1]
                        dict_list[j+1] = temp
                        
                elif A_or_D == 'D':
                    if dict_list[j]['MYCT'] < dict_list[j+1]['MYCT']:
                        temp = dict_list[j]
                        dict_list[j] = dict_list[j+1]
                        dict_list[j+1] = temp
        else:
            print("MYCT key is not present")
            return dict_list
    return dict_list # return the sorted list

#==========================================#
# Place your sort function after this line
def sort(list_dict: list, direction: str, which_function: str) -> str:
    """Return the opriginal list but sorted depeding on which function is chosen, and in the order of the chosen direction. If the input string is invalid, the function will return an error statement, and will return the orgibnal list.
    
    Pre conditions: dictionary == 'A' or 'D'
    
    Examples:
    
    >>> sort([{"CACH":10,"Model":"GP"},{"CACH":19.1,"Model":"MS"}],"D","CACH")
    [{"CACH": 19, "Model":"MS"}, {"CACH":10, "Model":"GP"}]
    
    >>>sort([{"Model":"GP"},{"Model":"MS"}], "D", "Model")
    Cannot be sorted by "Model"
    [{"Model":"GP"}, {"Model":"MS"}]
    """
    
    if which_function == 'CACH':
        return sort_cache_bubble(list_dict, direction)
    
    elif which_function == 'PRP':
        return sort_prp_selection(list_dict, direction)
    
    elif which_function == 'M_AVG':
        return sort_m_avg_insertion(list_dict, direction)
    
    elif which_function == 'MYCT':
        return sort_myct_bubble(list_dict, direction)    
    
    else:
        print('Cannot be sorted by', which_function)
        return list_dict

# Do NOT include a main script in your submission
