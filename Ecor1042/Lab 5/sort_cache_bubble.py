# ECOR 1042 Lab 5 - Individual submission for sort_cache_bubble

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Amina Hajiyeva"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101303729"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-082"

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

# Do NOT include a main script in your submission
