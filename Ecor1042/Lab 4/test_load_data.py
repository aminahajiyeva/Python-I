# ECOR 1042 Lab 4 - team submission

#import check module here
import check
#import load_data module here
from load_data import load_data, machine_vendor_list, machine_model_list, machine_cache_list, machine_prp_list, add_average_main_memory

# Update "" with your the name of the active members of the team
__author__ = "Charlie Tierney, Amina Hajiyeva, Shoubh Patel, John Samis"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-082"

#==========================================#

# Place test_return_list function here
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
                                # If the fun ction returns a list using isinstance(), set the outcome value of the check.equal() to an empty list.
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

# Place test_return_list_correct_lenght function here
def test_return_list_correct_lenght():
    """Retrn a series of test cases that return whether the given function has the correct length(s).
    
    """
    from load_data import machine_vendor_list
    check.equal(len(machine_vendor_list('machine-test.csv', 'burroughs')), 8)
    check.equal(len(machine_vendor_list('machine-test.csv', 'bti')), 2)
    check.equal(len(machine_vendor_list('machine-test.csv', 'amdahl')), 9)
    
    from load_data import machine_cache_list
    check.equal(len(machine_cache_list('machine-test.csv', 230)), 0)
    check.equal(len(machine_cache_list('machine-test.csv', 32)), 12)
    check.equal(len(machine_cache_list('machine-test.csv', 0)), 22)
    
    from load_data import machine_prp_list
    check.equal(len(machine_prp_list('machine-test.csv', 269)), 6)
    check.equal(len(machine_prp_list('machine-test.csv', 0)), 22)
    check.equal(len(machine_prp_list('machine-test.csv', 1000.0)), 1)
    
    from load_data import machine_model_list
    check.equal(len(machine_model_list('machine-test.csv',"8000")),1)
    check.equal(len(machine_model_list('machine-test.csv',"b1955")),1)
    check.equal(len(machine_model_list('machine-test.csv',"470v/7")),1)
    
    from load_data import add_average_main_memory
    check.equal(len(add_average_main_memory([{'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'ERP':38}])),1)
    check.equal(len(add_average_main_memory([{'MMIN': 1000,'MMAX': 3000}])),1)    
    check.equal(len(add_average_main_memory([{'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 
    'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'ERP':10}])),1)
    
    from load_data import load_data
    check.equal(len(load_data('machine-test.csv', ('MYCT', 20))),0)
    check.equal(len(load_data('machine-test.csv', ('vendor',"basf"))),2)
    check.equal(len(load_data('machine-test.csv', ("ALL", 'bti'))),22)
    check.equal(len(load_data('machine-test.csv', ("cach",128))),2)
    check.equal(len(load_data('machine-test.csv', ('model',"580-5840"))),4)
    check.equal(len(load_data('machine-test.csv', ("PRP", 1000))),1)
    
    check.summary()
    

if __name__ == '__main__':
    test_return_list_correct_lenght()

#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    """
    Perform Unit testing on functions created in the last lab. Test 3 cases for each 
    function for a total of 15 cases. An additional 6 test cases for load data.
    """
    test_file = 'machine-test.csv' 

    #====================Vendor Function tests======================
    t1 = machine_vendor_list(test_file, 'apollo')
    check.equal(t1[0], {'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    check.equal(t1[-1], {'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    #check.equal(machine_vendor_list(test_file, 'adviser'), [{'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}])
    
    print(t1)
    t2 = machine_vendor_list(test_file, 'amdahl')
    check.equal(t2[0], {'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253})
    check.equal(t2[-1], {'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238})
    #check.equal(machine_vendor_list(test_file, 'amdahl'), [{'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}, {'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253}, {'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253}, {'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132}, {'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381}, {'Model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381}, {'Model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749}, {'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238}])
   
    t3 = machine_vendor_list(test_file, 'burroughs')
    check.equal(t3[0], {'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23})
    check.equal(t3[-1], {'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45})
    #check.equal(machine_vendor_list(test_file, 'burroughs'), [{'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23}, {'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29}, {'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'PRP': 31, 'ERP': 22}, {'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'PRP': 120, 'ERP': 124}, {'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'PRP': 30, 'ERP': 35}, {'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 33, 'ERP': 39}, {'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'PRP': 61, 'ERP': 40}, {'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}])

    #==================Model Function tests========================
    t4 = machine_model_list(test_file, '470v/7')
    check.equal(t4[0], {'Vendor': 'amdahl', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253})
    check.equal(t4[-1], {'Vendor': 'amdahl', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253})
    #check.equal(machine_model_list(test_file, '32/60'), [{'Vendor': 'adviser', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}])

    t5 = machine_model_list(test_file,'580-5840')
    check.equal(t5[0], {'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381})
    check.equal(t5[-1],  {'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238})
    #check.equal(machine_model_list(test_file,'580-5840'), [{'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381}])
    
    t6 = machine_model_list(test_file,'dn320')
    check.equal(t6[0], {'Vendor': 'apollo', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    check.equal(t6[-1], {'Vendor': 'apollo', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    #check.equal(machine_model_list(test_file,'4443'), [{'Vendor': 'ipl', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 8, 'PRP': 45, 'ERP': 44}])

    #=========================Cache function tests==========================
    t7 = machine_cache_list(test_file, 64)
    check.equal(t7[0],{'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 318, 'ERP': 290})
    check.equal(t7[-1], {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124})
    #check.equal(machine_cache_list(test_file, 256), [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'PRP': 198, 'ERP': 199}, {'Vendor': 'nas', 'Model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 603}])
    
    t8 = machine_cache_list(test_file, 32)
    check.equal(t8[0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253})
    check.equal(t8[-1], {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124})
    #check.equal(machine_cache_list(test_file, 32), [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'PRP': 198, 'ERP': 199}, {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 138, 'ERP': 117}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}, {'Vendor': 'cdc', 'Model': 'cyber:170/750', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'PRP': 274, 'ERP': 102}, {'Vendor': 'cdc', 'Model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'PRP': 368, 'ERP': 102}, {'Vendor': 'gould', 'Model': 'concept:32/8705', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 144, 'ERP': 75}, {'Vendor': 'gould', 'Model': 'concept:32/8750', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'PRP': 144, 'ERP': 113}, {'Vendor': 'gould', 'Model': 'concept:32/8780', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'PRP': 259, 'ERP': 157}, {'Vendor': 'honeywell', 'Model': 'dps:8/49', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 134, 'ERP': 175}, {'Vendor': 'honeywell', 'Model': 'dps:8/50', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 66, 'ERP': 57}, {'Vendor': 'honeywell', 'Model': 'dps:8/52', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 141, 'ERP': 181}, {'Vendor': 'honeywell', 'Model': 'dps:8/62', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 189, 'ERP': 181}, {'Vendor': 'ibm', 'Model': '3033:u', 'MYCT': 57, 'MMIN': 4000, 'MMAX': 24000, 'PRP': 237, 'ERP': 171}, {'Vendor': 'ibm', 'Model': '3081', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 465, 'ERP': 361}, {'Vendor': 'ibm', 'Model': '3081:d', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 465, 'ERP': 350}, {'Vendor': 'ibm', 'Model': '4381-2', 'MYCT': 17, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 133, 'ERP': 116}, {'Vendor': 'ipl', 'Model': '4480', 'MYCT': 50, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 136, 'ERP': 128}, {'Vendor': 'nas', 'Model': 'as/5000', 'MYCT': 92, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 62, 'ERP': 53}, {'Vendor': 'nas', 'Model': 'as/5000-e', 'MYCT': 92, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 60, 'ERP': 53}, {'Vendor': 'nas', 'Model': 'as/6150', 'MYCT': 60, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 86, 'ERP': 95}, {'Vendor': 'nas', 'Model': 'as/6620', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 16000, 'PRP': 74, 'ERP': 107}, {'Vendor': 'nas', 'Model': 'as/6630', 'MYCT': 60, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 93, 'ERP': 117}, {'Vendor': 'nas', 'Model': 'as/6650', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 111, 'ERP': 119}, {'Vendor': 'nas', 'Model': 'as/7000', 'MYCT': 72, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 143, 'ERP': 120}, {'Vendor': 'nas', 'Model': 'as/8040', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 214, 'ERP': 126}, {'Vendor': 'nas', 'Model': 'as/8050', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 277, 'ERP': 266}, {'Vendor': 'nas', 'Model': 'as/8060', 'MYCT': 35, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 370, 'ERP': 270}, {'Vendor': 'nas', 'Model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 426}, {'Vendor': 'nas', 'Model': 'as/9000-n', 'MYCT': 48, 'MMIN': 4000, 'MMAX': 24000, 'PRP': 214, 'ERP': 151}, {'Vendor': 'nas', 'Model': 'as/9040', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 326, 'ERP': 267}, {'Vendor': 'nas', 'Model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 603}, {'Vendor': 'ncr', 'Model': 'v8635', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 8000, 'PRP': 51, 'ERP': 80}, {'Vendor': 'ncr', 'Model': 'v8650', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 8000, 'PRP': 116, 'ERP': 80}, {'Vendor': 'ncr', 'Model': 'v8655', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 100, 'ERP': 142}, {'Vendor': 'ncr', 'Model': 'v8665', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 24000, 'PRP': 140, 'ERP': 281}, {'Vendor': 'ncr', 'Model': 'v8670', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 212, 'ERP': 190}, {'Vendor': 'nixdorf', 'Model': '8890/70', 'MYCT': 200, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 41, 'ERP': 67}, {'Vendor': 'prime', 'Model': '50-850-ii', 'MYCT': 160, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 109, 'ERP': 53}, {'Vendor': 'siemens', 'Model': '7.561', 'MYCT': 52, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 130, 'ERP': 99}, {'Vendor': 'siemens', 'Model': '7.870-2', 'MYCT': 59, 'MMIN': 4000, 'MMAX': 12000, 'PRP': 113, 'ERP': 81}, {'Vendor': 'siemens', 'Model': '7.872-2', 'MYCT': 59, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 188, 'ERP': 149}, {'Vendor': 'siemens', 'Model': '7.875-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 24000, 'PRP': 173, 'ERP': 183}, {'Vendor': 'siemens', 'Model': '7.880-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 248, 'ERP': 275}, {'Vendor': 'siemens', 'Model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 405, 'ERP': 382}, {'Vendor': 'sperry', 'Model': '1100/61-h1', 'MYCT': 116, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 70, 'ERP': 56}, {'Vendor': 'sperry', 'Model': '1100/82', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 208, 'ERP': 227}, {'Vendor': 'sperry', 'Model': '1100/83', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 307, 'ERP': 341}, {'Vendor': 'sperry', 'Model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'PRP': 397, 'ERP': 360}, {'Vendor': 'sperry', 'Model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'PRP': 915, 'ERP': 919}, {'Vendor': 'sperry', 'Model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'PRP': 1150, 'ERP': 978}, {'Vendor': 'sperry', 'Model': '90/80-model-3', 'MYCT': 98, 'MMIN': 1000, 'MMAX': 8000, 'PRP': 46, 'ERP': 50}, {'Vendor': 'wang', 'Model': 'vs-100', 'MYCT': 480, 'MMIN': 512, 'MMAX': 8000, 'PRP': 67, 'ERP': 47}])
    
    t9 = machine_cache_list(test_file, 0)
    check.equal(t9[0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253})
    check.equal(t9[-1], {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'PRP': 76, 'ERP': 45})
    #check.equal(machine_cache_list(test_file, 0), [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'PRP': 198, 'ERP': 199}, {'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}, {'Vendor': 'cdc', 'Model': 'cyber:170/750', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'PRP': 274, 'ERP': 102}, {'Vendor': 'cdc', 'Model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'PRP': 368, 'ERP': 102}, {'Vendor': 'gould', 'Model': 'concept:32/8780', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'PRP': 259, 'ERP': 157}, {'Vendor': 'nas', 'Model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 426}, {'Vendor': 'nas', 'Model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 603}, {'Vendor': 'ncr', 'Model': 'v8665', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 24000, 'PRP': 140, 'ERP': 281}, {'Vendor': 'ncr', 'Model': 'v8670', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 212, 'ERP': 190}, {'Vendor': 'siemens', 'Model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 405, 'ERP': 382}, {'Vendor': 'sperry', 'Model': '1100/83', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 307, 'ERP': 341}, {'Vendor': 'sperry', 'Model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'PRP': 397, 'ERP': 360}, {'Vendor': 'sperry', 'Model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'PRP': 915, 'ERP': 919}, {'Vendor': 'sperry', 'Model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'PRP': 1150, 'ERP': 978}])

    #==========================PRP function tests============================
    t10 = machine_prp_list(test_file, 269)
    #check.equal(t10[0], {'vendor': 'amdahl', 'model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253})
    #check.equal(t10[-1], {'vendor': 'amdahl', 'model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238})
    #check.equal(machine_prp_list(test_file, 172), [{'vendor': 'adviser', 'model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'ERP': 199}, {'vendor': 'amdahl', 'model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'vendor': 'amdahl', 'model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'vendor': 'amdahl', 'model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'vendor': 'amdahl', 'model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'vendor': 'amdahl', 'model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'vendor': 'amdahl', 'model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'vendor': 'cdc', 'model': 'cyber:170/750', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'cdc', 'model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'cdc', 'model': 'cyber:170/845', 'MYCT': 64, 'MMIN': 5240, 'MMAX': 20970, 'CACH': 30, 'ERP': 136}, {'vendor': 'gould', 'model': 'concept:32/8780', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'CACH': 128, 'ERP': 157}, {'vendor': 'honeywell', 'model': 'dps:8/62', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 32000, 'CACH': 32, 'ERP': 181}, {'vendor': 'ibm', 'model': '3033:u', 'MYCT': 57, 'MMIN': 4000, 'MMAX': 24000, 'CACH': 64, 'ERP': 171}, {'vendor': 'ibm', 'model': '3081', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 361}, {'vendor': 'ibm', 'model': '3081:d', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 350}, {'vendor': 'ibm', 'model': '3083:b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 0, 'ERP': 220}, {'vendor': 'ibm', 'model': '3083:e', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 0, 'ERP': 113}, {'vendor': 'nas', 'model': 'as/8040', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'ERP': 126}, {'vendor': 'nas', 'model': 'as/8050', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 266}, {'vendor': 'nas', 'model': 'as/8060', 'MYCT': 35, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 270}, {'vendor': 'nas', 'model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 128, 'ERP': 426}, {'vendor': 'nas', 'model': 'as/9000-n', 'MYCT': 48, 'MMIN': 4000, 'MMAX': 24000, 'CACH': 32, 'ERP': 151}, {'vendor': 'nas', 'model': 'as/9040', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 267}, {'vendor': 'nas', 'model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 256, 'ERP': 603}, {'vendor': 'ncr', 'model': 'v8670', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 128, 'ERP': 190}, {'vendor': 'siemens', 'model': '7.872-2', 'MYCT': 59, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 64, 'ERP': 149}, {'vendor': 'siemens', 'model': '7.875-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 24000, 'CACH': 32, 'ERP': 183}, {'vendor': 'siemens', 'model': '7.880-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 275}, {'vendor': 'siemens', 'model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 128, 'ERP': 382}, {'vendor': 'sperry', 'model': '1100/82', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'CACH': 48, 'ERP': 227}, {'vendor': 'sperry', 'model': '1100/83', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'CACH': 112, 'ERP': 341}, {'vendor': 'sperry', 'model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'CACH': 112, 'ERP': 360}, {'vendor': 'sperry', 'model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 96, 'ERP': 919}, {'vendor': 'sperry', 'model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 128, 'ERP': 978}])

    t11 = machine_prp_list(test_file, 220)
    #check.equal(t11[0], {'vendor': 'amdahl', 'model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253})
    #check.equal(t11[-1], {'vendor': 'amdahl', 'model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238})
    #check.equal(machine_prp_list(test_file, 198), [{'vendor': 'adviser', 'model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'ERP': 199}, {'vendor': 'amdahl', 'model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'vendor': 'amdahl', 'model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'vendor': 'amdahl', 'model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'vendor': 'amdahl', 'model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'vendor': 'amdahl', 'model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'vendor': 'cdc', 'model': 'cyber:170/750', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'cdc', 'model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'cdc', 'model': 'cyber:170/845', 'MYCT': 64, 'MMIN': 5240, 'MMAX': 20970, 'CACH': 30, 'ERP': 136}, {'vendor': 'gould', 'model': 'concept:32/8780', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'CACH': 128, 'ERP': 157}, {'vendor': 'ibm', 'model': '3033:u', 'MYCT': 57, 'MMIN': 4000, 'MMAX': 24000, 'CACH': 64, 'ERP': 171}, {'vendor': 'ibm', 'model': '3081', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 361}, {'vendor': 'ibm', 'model': '3081:d', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 350}, {'vendor': 'ibm', 'model': '3083:b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 0, 'ERP': 220}, {'vendor': 'nas', 'model': 'as/8040', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'ERP': 126}, {'vendor': 'nas', 'model': 'as/8050', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 266}, {'vendor': 'nas', 'model': 'as/8060', 'MYCT': 35, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 270}, {'vendor': 'nas', 'model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 128, 'ERP': 426}, {'vendor': 'nas', 'model': 'as/9000-n', 'MYCT': 48, 'MMIN': 4000, 'MMAX': 24000, 'CACH': 32, 'ERP': 151}, {'vendor': 'nas', 'model': 'as/9040', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 267}, {'vendor': 'nas', 'model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 256, 'ERP': 603}, {'vendor': 'ncr', 'model': 'v8670', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 128, 'ERP': 190}, {'vendor': 'siemens', 'model': '7.880-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 275}, {'vendor': 'siemens', 'model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 128, 'ERP': 382}, {'vendor': 'sperry', 'model': '1100/82', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'CACH': 48, 'ERP': 227}, {'vendor': 'sperry', 'model': '1100/83', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'CACH': 112, 'ERP': 341}, {'vendor': 'sperry', 'model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'CACH': 112, 'ERP': 360}, {'vendor': 'sperry', 'model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 96, 'ERP': 919}, {'vendor': 'sperry', 'model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 128, 'ERP': 978}])
    
    t12 = machine_prp_list(test_file, 19)
    #check.equal(t12[0], {'vendor': 'amdahl', 'model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253})
    #check.equal(t12[-1], {'vendor': 'burroughs', 'model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45})
    #check.equal(machine_prp_list(test_file, 36) , [{'vendor': 'amdahl', 'model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'vendor': 'amdahl', 'model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'vendor': 'amdahl', 'model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'vendor': 'cdc', 'model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'ibm', 'model': '3081', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 361}, {'vendor': 'ibm', 'model': '3081:d', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 350}, {'vendor': 'nas', 'model': 'as/8060', 'MYCT': 35, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 270}, {'vendor': 'nas', 'model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 128, 'ERP': 426}, {'vendor': 'nas', 'model': 'as/9040', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 267}, {'vendor': 'nas', 'model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 256, 'ERP': 603}, {'vendor': 'siemens', 'model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 128, 'ERP': 382}, {'vendor': 'sperry', 'model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'CACH': 112, 'ERP': 360}, {'vendor': 'sperry', 'model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 96, 'ERP': 919}, {'vendor': 'sperry', 'model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 128, 'ERP': 978}])

    #=========================add_average_main_memory tests=======================
    t13 = add_average_main_memory(machine_cache_list(test_file, 32))
    check.equal(t13[0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253, 'M_AVG': 20000.0})
    check.equal(t13[-1], {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124, 'M_AVG': 5000.0})

    t14 = add_average_main_memory(machine_model_list(test_file,'8000'))
    check.equal(t14[0], {'Vendor': 'bti', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64, 'M_AVG': 8256.0})
    check.equal(t14[-1],{'Vendor': 'bti', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64, 'M_AVG': 8256.0})

    t15 = add_average_main_memory(load_data(test_file, ('PRP', 19)))
    #check.equal(t15[0], {'vendor': 'amdahl', 'model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253, 'M_AVG': 20000.0})
    #check.equal(t15[-1],  {'vendor': 'burroughs', 'model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45, 'M_AVG': 4650.0})

    #=========================Load data function tests========================
    t16 = load_data('machine-test.csv', ('PRP', 19))
    #check.equal(t16[0], {'vendor': 'amdahl', 'model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253})
    #check.equal(t16[-1], {'vendor': 'burroughs', 'model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45})

    t17 = load_data(test_file, ('CACH', 32))
    check.equal(t17[0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253})
    check.equal(t17[-1], {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124})

    #check.equal(load_data(test_file, ('PRP', 150)), [{'vendor': 'amdahl', 'model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'vendor': 'amdahl', 'model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'vendor': 'amdahl', 'model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'vendor': 'cdc', 'model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'ibm', 'model': '3081', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 361}, {'vendor': 'ibm', 'model': '3081:d', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 350}, {'vendor': 'nas', 'model': 'as/8060', 'MYCT': 35, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 270}, {'vendor': 'nas', 'model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 128, 'ERP': 426}, {'vendor': 'nas', 'model': 'as/9040', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 267}, {'vendor': 'nas', 'model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 256, 'ERP': 603}, {'vendor': 'siemens', 'model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 128, 'ERP': 382}, {'vendor': 'sperry', 'model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'CACH': 112, 'ERP': 360}, {'vendor': 'sperry', 'model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 96, 'ERP': 919}, {'vendor': 'sperry', 'model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 128, 'ERP': 978}][{'vendor': 'adviser', 'model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'ERP': 199}, {'vendor': 'amdahl', 'model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'vendor': 'amdahl', 'model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'vendor': 'amdahl', 'model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'vendor': 'amdahl', 'model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'vendor': 'amdahl', 'model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'vendor': 'amdahl', 'model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'vendor': 'cdc', 'model': 'cyber:170/750', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'cdc', 'model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'cdc', 'model': 'cyber:170/845', 'MYCT': 64, 'MMIN': 5240, 'MMAX': 20970, 'CACH': 30, 'ERP': 136}, {'vendor': 'gould', 'model': 'concept:32/8780', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'CACH': 128, 'ERP': 157}, {'vendor': 'honeywell', 'model': 'dps:8/62', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 32000, 'CACH': 32, 'ERP': 181}, {'vendor': 'ibm', 'model': '3033:u', 'MYCT': 57, 'MMIN': 4000, 'MMAX': 24000, 'CACH': 64, 'ERP': 171}, {'vendor': 'ibm', 'model': '3081', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 361}, {'vendor': 'ibm', 'model': '3081:d', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 350}, {'vendor': 'ibm', 'model': '3083:b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 0, 'ERP': 220}, {'vendor': 'ibm', 'model': '3083:e', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 0, 'ERP': 113}, {'vendor': 'nas', 'model': 'as/8040', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'ERP': 126}, {'vendor': 'nas', 'model': 'as/8050', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 266}, {'vendor': 'nas', 'model': 'as/8060', 'MYCT': 35, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 270}, {'vendor': 'nas', 'model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 128, 'ERP': 426}, {'vendor': 'nas', 'model': 'as/9000-n', 'MYCT': 48, 'MMIN': 4000, 'MMAX': 24000, 'CACH': 32, 'ERP': 151}, {'vendor': 'nas', 'model': 'as/9040', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 267}, {'vendor': 'nas', 'model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 256, 'ERP': 603}, {'vendor': 'ncr', 'model': 'v8670', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 128, 'ERP': 190}, {'vendor': 'siemens', 'model': '7.872-2', 'MYCT': 59, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 64, 'ERP': 149}, {'vendor': 'siemens', 'model': '7.875-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 24000, 'CACH': 32, 'ERP': 183}, {'vendor': 'siemens', 'model': '7.880-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 275}, {'vendor': 'siemens', 'model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 128, 'ERP': 382}, {'vendor': 'sperry', 'model': '1100/82', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'CACH': 48, 'ERP': 227}, {'vendor': 'sperry', 'model': '1100/83', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'CACH': 112, 'ERP': 341}, {'vendor': 'sperry', 'model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'CACH': 112, 'ERP': 360}, {'vendor': 'sperry', 'model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 96, 'ERP': 919}, {'vendor': 'sperry', 'model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 128, 'ERP': 978}])
    #check.equal(load_data(test_file, ('CACH', 32)), [{'vendor': 'amdahl', 'model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'vendor': 'amdahl', 'model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'vendor': 'amdahl', 'model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'vendor': 'amdahl', 'model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'vendor': 'cdc', 'model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'CACH': 131, 'ERP': 102}, {'vendor': 'ibm', 'model': '3081', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 361}, {'vendor': 'ibm', 'model': '3081:d', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 350}, {'vendor': 'nas', 'model': 'as/8060', 'MYCT': 35, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 270}, {'vendor': 'nas', 'model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 128, 'ERP': 426}, {'vendor': 'nas', 'model': 'as/9040', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 267}, {'vendor': 'nas', 'model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 256, 'ERP': 603}, {'vendor': 'siemens', 'model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 128, 'ERP': 382}, {'vendor': 'sperry', 'model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'CACH': 112, 'ERP': 360}, {'vendor': 'sperry', 'model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 96, 'ERP': 919}, {'vendor': 'sperry', 'model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'CACH': 128, 'ERP': 978}][{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'PRP': 198, 'ERP': 199}, {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5860', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 138, 'ERP': 117}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}, {'Vendor': 'cdc', 'Model': 'cyber:170/750', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'PRP': 274, 'ERP': 102}, {'Vendor': 'cdc', 'Model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'PRP': 368, 'ERP': 102}, {'Vendor': 'gould', 'Model': 'concept:32/8705', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 144, 'ERP': 75}, {'Vendor': 'gould', 'Model': 'concept:32/8750', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'PRP': 144, 'ERP': 113}, {'Vendor': 'gould', 'Model': 'concept:32/8780', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'PRP': 259, 'ERP': 157}, {'Vendor': 'honeywell', 'Model': 'dps:8/49', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 134, 'ERP': 175}, {'Vendor': 'honeywell', 'Model': 'dps:8/50', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 66, 'ERP': 57}, {'Vendor': 'honeywell', 'Model': 'dps:8/52', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 141, 'ERP': 181}, {'Vendor': 'honeywell', 'Model': 'dps:8/62', 'MYCT': 140, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 189, 'ERP': 181}, {'Vendor': 'ibm', 'Model': '3033:u', 'MYCT': 57, 'MMIN': 4000, 'MMAX': 24000, 'PRP': 237, 'ERP': 171}, {'Vendor': 'ibm', 'Model': '3081', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 465, 'ERP': 361}, {'Vendor': 'ibm', 'Model': '3081:d', 'MYCT': 26, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 465, 'ERP': 350}, {'Vendor': 'ibm', 'Model': '4381-2', 'MYCT': 17, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 133, 'ERP': 116}, {'Vendor': 'ipl', 'Model': '4480', 'MYCT': 50, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 136, 'ERP': 128}, {'Vendor': 'nas', 'Model': 'as/5000', 'MYCT': 92, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 62, 'ERP': 53}, {'Vendor': 'nas', 'Model': 'as/5000-e', 'MYCT': 92, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 60, 'ERP': 53}, {'Vendor': 'nas', 'Model': 'as/6150', 'MYCT': 60, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 86, 'ERP': 95}, {'Vendor': 'nas', 'Model': 'as/6620', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 16000, 'PRP': 74, 'ERP': 107}, {'Vendor': 'nas', 'Model': 'as/6630', 'MYCT': 60, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 93, 'ERP': 117}, {'Vendor': 'nas', 'Model': 'as/6650', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 111, 'ERP': 119}, {'Vendor': 'nas', 'Model': 'as/7000', 'MYCT': 72, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 143, 'ERP': 120}, {'Vendor': 'nas', 'Model': 'as/8040', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 214, 'ERP': 126}, {'Vendor': 'nas', 'Model': 'as/8050', 'MYCT': 40, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 277, 'ERP': 266}, {'Vendor': 'nas', 'Model': 'as/8060', 'MYCT': 35, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 370, 'ERP': 270}, {'Vendor': 'nas', 'Model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 426}, {'Vendor': 'nas', 'Model': 'as/9000-n', 'MYCT': 48, 'MMIN': 4000, 'MMAX': 24000, 'PRP': 214, 'ERP': 151}, {'Vendor': 'nas', 'Model': 'as/9040', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 326, 'ERP': 267}, {'Vendor': 'nas', 'Model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 603}, {'Vendor': 'ncr', 'Model': 'v8635', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 8000, 'PRP': 51, 'ERP': 80}, {'Vendor': 'ncr', 'Model': 'v8650', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 8000, 'PRP': 116, 'ERP': 80}, {'Vendor': 'ncr', 'Model': 'v8655', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 100, 'ERP': 142}, {'Vendor': 'ncr', 'Model': 'v8665', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 24000, 'PRP': 140, 'ERP': 281}, {'Vendor': 'ncr', 'Model': 'v8670', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 212, 'ERP': 190}, {'Vendor': 'nixdorf', 'Model': '8890/70', 'MYCT': 200, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 41, 'ERP': 67}, {'Vendor': 'prime', 'Model': '50-850-ii', 'MYCT': 160, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 109, 'ERP': 53}, {'Vendor': 'siemens', 'Model': '7.561', 'MYCT': 52, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 130, 'ERP': 99}, {'Vendor': 'siemens', 'Model': '7.870-2', 'MYCT': 59, 'MMIN': 4000, 'MMAX': 12000, 'PRP': 113, 'ERP': 81}, {'Vendor': 'siemens', 'Model': '7.872-2', 'MYCT': 59, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 188, 'ERP': 149}, {'Vendor': 'siemens', 'Model': '7.875-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 24000, 'PRP': 173, 'ERP': 183}, {'Vendor': 'siemens', 'Model': '7.880-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 248, 'ERP': 275}, {'Vendor': 'siemens', 'Model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 405, 'ERP': 382}, {'Vendor': 'sperry', 'Model': '1100/61-h1', 'MYCT': 116, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 70, 'ERP': 56}, {'Vendor': 'sperry', 'Model': '1100/82', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 208, 'ERP': 227}, {'Vendor': 'sperry', 'Model': '1100/83', 'MYCT': 50, 'MMIN': 2000, 'MMAX': 32000, 'PRP': 307, 'ERP': 341}, {'Vendor': 'sperry', 'Model': '1100/84', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 32000, 'PRP': 397, 'ERP': 360}, {'Vendor': 'sperry', 'Model': '1100/93', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'PRP': 915, 'ERP': 919}, {'Vendor': 'sperry', 'Model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'PRP': 1150, 'ERP': 978}, {'Vendor': 'sperry', 'Model': '90/80-model-3', 'MYCT': 98, 'MMIN': 1000, 'MMAX': 8000, 'PRP': 46, 'ERP': 50}, {'Vendor': 'wang', 'Model': 'vs-100', 'MYCT': 480, 'MMIN': 512, 'MMAX': 8000, 'PRP': 67, 'ERP': 47}])

    t18 = load_data(test_file, ('ALL', 69))
    check.equal(t18[0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253})
    check.equal(t18[-1], {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45})

    t19 = load_data(test_file, ('VENDOR', 'apollo'))
    check.equal(t19[0], {'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    check.equal(t19[-1], {'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})

    t20 = load_data(test_file, ('MODEL', '580-5840'))
    check.equal(t20[0], {'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381})
    check.equal(t20[-1], {'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238})

    t21 = load_data(test_file, ('ALL', '32/60'))
    check.equal(t21[0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253})
    check.equal(t21[-1], {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45})

    check.summary()

if __name__ == '__main__':
    test_return_correct_dict_inside_list()

#Place test_add_average function here

def test_add_average():  # Complete the function with your test cases

    check.equal((len(load_data('machine-test.csv', ('PRP', 0)))),
        len(add_average_main_memory((load_data('machine-test.csv', ('PRP', 0))))))

 

    check.equal((len(load_data('machine-test.csv', ('Model', '')))),
        len(add_average_main_memory((load_data('machine-test.csv', ('Model', ''))))))

 

    check.equal((len(load_data('machine-test.csv', ('Vendor', '')))),
        len(add_average_main_memory((load_data('machine-test.csv', ('Vendor', ''))))))

 

    check.equal((len(load_data('machine-test.csv', ('CACH', 0)))),
        len(add_average_main_memory((load_data('machine-test.csv', ('CACH', 0))))))

 

    check.equal((len(load_data('machine-test.csv',
    ('Vendor', 'ad')))), len(add_average_main_memory([])))

 

    check.equal((len(load_data('machine-test.csv', ('All', '')))),
        len(add_average_main_memory((load_data('machine-test.csv', ('All', ''))))))

 

    # Check if there is exactly one more key in the dictonary

 

    check.equal((len(load_data('machine-test.csv', ('PRP', 1144))[-1]) + 1), (len(add_average_main_memory(
        load_data('machine-test.csv', ('PRP', 1144)))[-1])))

 

    check.equal((len(load_data('machine-test.csv', ('Model', '8000'))[-1]) + 1), (len(add_average_main_memory(
        load_data('machine-test.csv', ('Model', '8000')))[-1])))

 

    check.equal((len(load_data('machine-test.csv', ('Vendor', 'apollo'))[-1]) + 1), (len(add_average_main_memory(
        load_data('machine-test.csv', ('Vendor', 'apollo')))[-1])))

 

    check.equal((len(load_data('machine-test.csv', ('CACH', 142))[-1]) + 1), (len(add_average_main_memory(
        load_data('machine-test.csv', ('CACH', 0)))[-1])))

 

    check.equal((len(load_data('machine-test.csv', ('All', ''))[-1]) + 1), (len(add_average_main_memory(
        load_data('machine-test.csv', ('All', '')))[-1])))

 

    # Check if M_AVG is properly calculated

    check.within(((32000 + 64000) / 2), (((add_average_main_memory(

        load_data('machine-test.csv', ('PRP', 1144)))[-1]))['M_AVG']), 0.001)

    check.within(((512 + 16000) / 2), (((add_average_main_memory(

        load_data('machine-test.csv', ('Model', '8000')))[-1]))['M_AVG']), 0.001)

    check.within(((1000 + 3000) / 2), (((add_average_main_memory(

        load_data('machine-test.csv', ('Vendor', 'apollo')))[-1]))['M_AVG']), 0.001)

    check.within(((5000 + 5000) / 2), (((add_average_main_memory(
        load_data('machine-test.csv', ('CACH', 142)))[-1]))['M_AVG']), 0.001)

    check.within(((3100 + 6200) / 2), (((add_average_main_memory(
        load_data('machine-test.csv', ('All', '')))[-1]))['M_AVG']), 0.001)

if __name__ == '__main__':
    test_add_average()

check.summary()


# Do NOT include a main script in your submission
