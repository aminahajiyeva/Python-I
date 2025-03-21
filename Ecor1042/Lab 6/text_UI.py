# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Shoubh Patel"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101299720"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-82"

#==========================================#
# Place your script for your text_UI after this line
import load_data as data
import sort as sort
import histogram as hist
import curve_fit as curve


def text_UI():
    """
    Return data according to the users input, if L returns data in accordance to filter provided, if S
    sorts the data in ascending in descending order from the Load data list, if C returns a Curve to the parameter the user sets, if H
    returns a histogram in accordance to user input, if E terminates program

    Examples:
    Use the inputs the function does not take any arguments so not examples can be provided
    """
    x = 'placeholder'  # Sets x to a string
    # keeps loaded_data as a set variable so the function doesnt call a non existent variable later
    loaded_data = 'placeholder'
    while x != 'E' or x != 'e':  # Continute the loop as long as the user doesnt input 'E' or 'e'
        x = input('The available commands are:\n L) oad data\n S) ort data\n C) urve fit\n H) istogram\n E) xit\nPlease type your command: ')
        if x == 'L' or x == 'l':
            # Tells the code what file to read from later on
            filename = input('Please enter the name of the file: ')
            attribute_filter = input(
                'Please enter the attribute to use as a filter: ')

            if attribute_filter == 'All':  # Runs this function if All is selected
                loaded_data = (data.add_average_main_memory(
                    data.load_data(filename, ('All', ''))))
                print('Data loaded')

            elif attribute_filter == 'CACH' or attribute_filter == 'PRP':
                attribute_value = input(
                    'Please enter the value of the attribute: ')
                loaded_data = (data.add_average_main_memory(data.load_data(
                    filename, (attribute_filter, int(attribute_value)))))
                print('Data loaded')

            elif attribute_filter == 'Vendor' or attribute_filter == 'Model':
                attribute_value = input(
                    'Please enter the value of the attribute: ')
                loaded_data = (data.add_average_main_memory(data.load_data(
                    filename, (attribute_filter, (attribute_value)))))
                print('Data loaded')

            else:
                print('attribute is invalid, please enter a new attribute')

        elif x == 'S' or x == 's':  # Sort
            attribute_filter = input(
                'Please enter the attribute you want to use for sorting:\n "CACH", "PRP", "M_AVG", "MYCT": ')
            sort_method = input('Ascending (A) or Descending (D) order: ')
            if loaded_data == 'placeholder':  # Tells the user to load data if they havent before
                print('File not loaded. Please load a file first')
            elif attribute_filter == 'CACH' or attribute_filter == 'PRP' or attribute_filter == 'M_AVG' or attribute_filter == 'MYCT':
                display_data = input(
                    'Data sorted. Do you want to display the data?: ')
                print(sort.sort(loaded_data, sort_method, attribute_filter))
            else:
                print('Invalid command')

        elif x == 'C' or x == 'c':  # Curve fit
            if loaded_data == 'placeholder':  # Tells the user that no file has been loaded
                print('File not loaded. Please load a file first')
            else:
                attribute_filter = input(
                    'Please enter the attribute you want to use to find the best fit for "M_AVG":  ')
                degree_order = input(
                    'Please enter the order of polynomial to be fitted: ')
                print(curve.curve_fit(loaded_data,
                      attribute_filter, int(degree_order)))

        elif x == 'H' or x == 'h':  # Histogram
            if loaded_data == 'placeholder':
                print('File not loaded. Please load a file first')
            else:
                # Prints a histogram in accordance to user specifications
                attribute_filter = input(
                    'Please enter the attribute you want to use for plotting: ')
                print(hist.histogram(loaded_data, str(attribute_filter)))

        elif x == 'E' or x == 'e':
            return 'Program terminated'  # Stops the program is user inputs 'E' or 'e'

        else:
            print('Invalid command, please enter a different command')


text_UI()
