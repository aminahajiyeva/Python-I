 """
            for i in range(len(machine_dic_list) - 1):
                if machine_dic_list[i] > machine_dic_list[i + 1]:
                    # swap the variables using a place holder variable to not loose the value
                    place_holder = machine_dic_list[i]
                    machine_dic_list[i] = machine_dic_list[i + 1]
                    machine_dic_list[i + 1] = place_holder
                    # revert swap variable back to True to continue looping through indexes.
                    swap = True
                    
    # if the user wants to sort the list decsendingly, and the list entry is valid:
    elif order_of_list.upper() == "D" and list_of_keys[5] == "CACH":
        # create a variable that will determine when the list is sorted.
        swap = True
        # while the list is not sorted, change the value of the varible to False to indicate this.
        while swap:
            swap = False
            # for the list, if the current index evaluated is less than the next one, swap them
            for i in range(len(machine_dic_list) - 1):
                if machine_dic_list[i] < machine_dic_list[i + 1]:
                    # swap the variables using a place holder variable to not loose the value
                    place_holder = machine_dic_list[i]
                    machine_dic_list[i] = machine_dic_list[i + 1]
                    machine_dic_list[i + 1] = place_holder
                    # revert swap variable back to True to continue looping through indexes.
                    swap = True
    """
 
 """
 if len(machine_dic_list) > 1:
     # for the list, if the current index evaluated is greater than the next one, swap them 
     for i in range(len(machine_dic_list) - 1):
         for j in range(0, len(machine_dic_list) - i - 1):
             while swap:
                 swap = False
                 if order_of_list.upper() == "A" :
                         if machine_dic_list[j]['CACH'] > machine_dic_list[j + 1]['CACH']:
                             # swap the variables using a place holder variable to not loose the value
                             place_holder = machine_dic_list[j]
                             machine_dic_list[j] = machine_dic_list[j + 1]
                             machine_dic_list[j + 1] = place_holder
                             # revert swap variable back to True to continue looping through indexes.
                             swap = True
                             
                 elif order_of_list.upper() == "D" and machine_dic_list[j]['CACH'] and machine_dic_list[j + 1]['CACH']:
                         if machine_dic_list[j]['CACH'] < machine_dic_list[j + 1]['CACH']:
                             # swap the variables using a place holder variable to not loose the value
                             place_holder = machine_dic_list[j]
                             machine_dic_list[j] = machine_dic_list[j + 1]
                             machine_dic_list[j + 1] = place_holder
                             # revert swap variable back to True to continue looping through indexes.
                             swap = True

                  # if the user fails to provide a valid list, inform them of this
                 else:
                     print("'CACH' key is not present")
                     swap = False
             j += 1
         i += 1                        
         """
         # return the sorted list, or if no valid entry return the original list
 #return machine_dic_list 