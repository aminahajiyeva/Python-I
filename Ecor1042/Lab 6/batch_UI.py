# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "John Alexander Samis"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101274169"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-082"

#==========================================#
# Place your script for your batch_UI after this line


import load_data
import sort
import curve_fit
import histogram

def batch_UI():
    """
    Create a text user interface in which input will be taken from a user's text file.
    This function utilizes a 'full command' every line as its input and executes 
    depending on the contents of the text file.

    Preconditions: 
    Assume the file contains no errors and commands are valid.
    Assume letter inputs are uppercase.
    Assume commands are seperated by a ';'.
"""

    txt_file = input("Please enter the name of the file where your commands are stored: ")
    file = open(txt_file, 'r')
    file_commands = []

    for line in file:
        values = line.strip('\n').split(';')
        file_commands += [values]
    file.close()

    for value in file_commands:
        if value[0].upper() == "L":
            l_data = load_data.load_data(value[1], (value[2], value[3]))
            print("Data loaded")
        elif value[0].upper() == "S":
            s_data = sort.sort(l_data, value[2], value[1])
            print("Data Sorted")
            if value[3].upper() == "Y":
                for machine in s_data:
                    print(machine)
        elif value[0].upper() == "H":
            hist = histogram.histogram(l_data, value[1])
            print("The Histogram is displayed")
        elif value[0].upper() == "C":
            curve = curve_fit.curve_fit(l_data, value[1], value[2])
            print("Curve fitted")

if __name__ == "__main__":
    batch_UI()