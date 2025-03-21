# ECOR 1042 Lab 3 - Template

# Update
__author__ = "Amina Hajiyeva"
__student_number__ = "101303729"
__team__ = "T082"

#==========================================#
# Place your machine_cache_list function after this line

# Do not include a main script

def machine_cache_list(file_name: str, memory_cache: int) -> dict:
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
