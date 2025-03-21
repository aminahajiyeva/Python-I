# ECOR 1042 Lab 3 - Template


# Update "" to list all students contributing to the team work
__author__ = "Charlie Tierney, Amina Hajiyeva, Shoubh Patel, John Samis"

# Update "" with your team (e.g. T102)
__team__ = "T82"
import string
#==========================================#
# Place your machine_vendor_list function after this line
def machine_vendor_list(filename: str, vendor: str) -> list:
    """Return a list of machines that belong to the vendor from a file provided. 
    
    preconditions: N/A
    
    Examples: 
    
    >>> machine_vendor_list('machine.csv', 'adviser')
    [ {'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256,
    'PRP': 198, 'ERP':199} ]
     """
    list_of_machines = [ ]
    
    file = open(filename, 'r')
    headers = file.readline().strip().split(',')
    print(headers)
    for line in file:
        if vendor in line:
            values = line.strip().split(',')
            machines = {}
            for i in range(1, len(headers)):
                try:
                    machines[headers[i]] = int(values[i])
                except:
                    machines[headers[i]] = (values[i])
            list_of_machines.append(machines)
    
    file.close
    return list_of_machines     

#==========================================#
# Place your machine_model_list function after this line
def machine_model_list(file_name: str, machine_model: str) -> list:
    """
    Return a list of machines whose model is the one provided as its parameter (stored as a dictionnary).
    The keys of the dictionnary are the labels for all the attributes except for 'Model'. 
    If no machines satisfy the model values in the function argument, return an empty list.

    Preconditions: Assume data loaded has no errors. Assume the data has the same shape provided in "machine.csv". 
        Assume the data has no duplicate entries.
    Examples: 
    >>>machine_model_list('machine.csv', '32/60')
    [{'Vendor': 'adviser', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}]

    """
    
    
    final_list = []
    file = open(file_name, 'r')
    count = 0
    
    
    for line in file:
        line = line.replace("\n","").split(",")
        if count == 0:
            titles = line
            count+=1

        elif machine_model == line[1]:
            model_dict = {}
            model_dict[titles[0]] = line[0] 
            model_dict[titles[2]] = int(line[2])
            model_dict[titles[3]] = int(line[3])
            model_dict[titles[4]] = int(line[4])
            model_dict[titles[5]] = int(line[5])
            model_dict[titles[6]] = int(line[6])
            model_dict[titles[7]] = int(line[7])
            final_list.append(model_dict)

    file.close()
    return final_list

#==========================================#
# Place your machine_cache_list function after this line
def machine_cache_list(file_name: str, memory_cache: int) -> list:
    """
    Return a list of machines with their respective memory cache provided.
    Precondition:
    >>> machine_cache_list('machine.csv', 128)
    [ {'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256,
    'MMAX': 6000, 'PRP': 198, 'ERP':199},
    {another element},…]
     >>> machine_cache_list('machine.csv', 64)
    [ {'Vendor': 'amdahl', 'Model': '470v / b', 'MYCT': 26, 'MMIN': 8000,
    'MMAX': 32000, 'PRP': 318, 'ERP':290},
    {another element},…]
     >>> machine_cache_list('machine.csv', 131)
    [ {'Vendor': 'cdc', 'Model': 'cyber: 170 / 750', 'MYCT': 25, 'MMIN': 1310,
    'MMAX': 2620, 'PRP': 274, 'ERP':102},
    {another element},…]
    """

    # create empty list to store data from file, create another one to store the machines with the given cache
    machine_list = []

    # open the myfile by reading it
    myfile = open(file_name, 'r')

    # create variable holding the header, keys of all the columns, the number of keys(columns)
    header = myfile.readline().replace("\n", "").split(
        ",")  # ["Vendor", "Machine","MYCT"]
    
    # get data from the csv myfile
    for line in myfile:

        # "Vendor, Model, MYCT, MMIN, MMAX, CACH, PRP, ERP"
        line = line.split(",")

        # if the memory cache matches the given, add the machine to the dictionary
        if int(line[5]) >= memory_cache:
            machine = {}
            machine[header[0]] = line[0]
            machine[header[1]] = line[1]
            machine[header[2]] = int(line[2])
            machine[header[3]] = int(line[3])
            machine[header[4]] = int(line[4])
            machine[header[6]] = int(line[6])
            machine[header[7]] = int(line[7])
            machine_list.append(machine)

    # close the myfile
    myfile.close()

    # return the new dictionary with the machines containing the required cache
    return machine_list


#==========================================#
# Place your machine_prp_list function after this line

def machine_prp_list(filename: str, prp: int) -> list:

    """
    Return a dictonary containing vendoers, models, MYCT, MMIN, MMAX, CACHE
    , and ERP if the prp value is greater then or equal to the specified
    number

    >>>machine_prp_list('machine.csv', 1150)

    {'Vendors': 'sperry', 'models': '1100/94', 'MYCT': 8000, 'MMIN':
    """

    infile = open(filename, 'r')
    Values_prps = []

    for line in infile:
        line = line.split(',')
        list_of_values = list(line)
        if (list_of_values[6]) == 'PRP' or list_of_values[6] == 'None':
            pass
        elif int(list_of_values[6]) >= prp:
            Values_prps += [{'vendor': list_of_values[0], 'model': list_of_values[1], 'MYCT': int(list_of_values[2]),
                    'MMIN': int(list_of_values[3]), 'MMAX': int(list_of_values[4]), 'CACH': int(list_of_values[5]), 'ERP': int(list_of_values[7])}]
        else:
            int(list_of_values[6]) < prp
            pass
    infile.close()
    return(Values_prps)

#==========================================#
# Place your load_data function after this line

def load_data(filename: str, function: tuple) -> list:
    """ 
    Return a list of machines stored in a dictionary in which keys are the labels for attributes in the dataset
    except for the first item of the tuple in the function call.
    Allows user to choose what data is to be loaded. 

    Precondition: None

    Examples:
    >>>load_data('machine.csv', ('PRP', 150))
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256: 'ERP': 199}]
    """
    
    valid_attributes = ['Vendor', 'Model', 'CACH', 'PRP', 'ALL'] 
    
    attribute, filter_value = function
          
                    
    if attribute.upper() == 'VENDOR':
        return machine_vendor_list(filename, filter_value)
        
        
    elif attribute.upper() == 'MODEL':
        return machine_model_list(filename, filter_value)
        
    elif attribute.upper() == 'CACH':
        return machine_cache_list(filename, filter_value)
        
    elif attribute.upper() == 'PRP':
        return  machine_prp_list(filename, filter_value)
        
    elif attribute.upper() == 'ALL':
        list_of_machines = []
        file = open(filename, 'r')
        file = file.readlines()
        headers = file[0].strip().split(',')
        for line in file:
            values = line.strip().split(',')
            machines = {}
            for i in range(0, len(headers)):
                try:
                    machines[headers[i]] = int(values[i])
                except:
                    machines[headers[i]] = (values[i])
            list_of_machines.append(machines)
        
        del list_of_machines[0]
        
        return list_of_machines
                        
    else: 
        return []
    
#==========================================#
# Place your add_average_main_memory function after this line

def add_average_main_memory(machine_list):
    """
    Return the inputted list with an updated dictionary with average main memory added.
    Round to two decimal spaces.

    Preconditions: None

    Example:
    >>>add_average_main_memory('PRP')
    [ {'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256,
    'MMAX': 6000, 'CACH': 256, 'ERP':199, 'M_AVG': 3128.0}]

      
    """
    
    for list_of_machines in machine_list:
        average = (list_of_machines['MMIN'] + list_of_machines['MMAX']) / 2
        list_of_machines['M_AVG'] = average 
    return machine_list


# Do NOT include a main script in your submission


