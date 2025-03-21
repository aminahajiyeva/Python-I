# ECOR 1042 Lab 4 - Individual submission for test1 function

#import check module here

import check

# import load_data module here

from load_data import load_data, machine_vendor_list, machine_model_list, machine_cache_list, machine_prp_list, add_average_main_memory

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Amina Hajiyeva"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101303729"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-082"

#==========================================#
#Do not modify the code alreayd provided.

def test_return_list():
    # Complete the function with your test cases

        # open the file required for testing, set it to a variable to be able to call it
        file_name = "machine-test.csv"
        # create an list with default values to be able to put it as a paramater for whichever function needs it
        values_given = ["vendor", "advisor"]
        # put all functions into a list, to be able to iterate through all of them easily
        functions = [load_data, machine_vendor_list,
                machine_model_list, machine_cache_list, machine_prp_list,add_average_main_memory]
        # number of test cases for each function
        test_cases = [6, 3, 3, 3, 3, 3, 3]
        # create a boolean that will be used to output whether the return value is a list or not
        is_list = False

        # for the number of functions given, set the current function equal to the variable current_function to later be able to evaluate it individually. Additonally, set the num_test value equal to the total number of tests for the respective function
        for i in range(len(functions)):
                current_function = functions[i]
                num_tests = test_cases[i]
                # if the current function evaluated is load_data, as a parameter put the test file name as well as the default list defined above.
                if current_function == load_data:
                        for i in range(num_tests):
                                result = current_function(file_name, values_given)
                                # If the function returns a list using isinstance(), set the outcome value of the check.equal() to an empty list.
                                is_list = isinstance(result, list)
                                if is_list == True:
                                        result = []
                                check.equal(result, [])

                # for the functions whose parameters are two strings
                elif current_function == machine_vendor_list or current_function == machine_model_list:
                        for i in range(num_tests):
                                # since parameter for the functions require the file name and a string, pass the file name as well as a default empty string as parameters
                                result = current_function(file_name, "")
                                # If the function returns a list using isinstance(), set the outcome value of the check.equal() to an empty list.
                                is_list = isinstance(result, list)
                                if is_list == True:
                                        result = []
                                check.equal(result, [])
                                
                # for the functions whose parameters are a string and an int
                elif current_function == machine_cache_list or current_function == machine_prp_list:
                        for i in range(num_tests):
                                # since parameter for the functions require the file name and an int, pass the file name as well as a default int value of 0 as parameters
                                result = current_function(file_name, 0)
                                # If the function returns a list using isinstance(), set the outcome value of the check.equal() to an empty list.
                                is_list = isinstance(result, list)
                                if is_list == True:
                                        result = []
                                check.equal(result, [])
                                
                # for the function add_average_main_memory, go through its designated number of tests
                else:
                        for i in range(num_tests):
                                # the parameter for this function is a list, so fill it with a default value of an empty list
                                result = current_function([])
                                # using isinstance determine if the function returns a list and if it does set the result equal to an empty list, use check.equal to verify
                                is_list = isinstance(result, list)
                                if is_list == True:
                                        result = []
                                check.equal(result, [])

        # determines when code above is to be executed
        if __name__ == 'load_data':
                test_return_list()

        # output the result of all the check functions run
        check.summary()
        
# Do NOT include a main script in your submission
