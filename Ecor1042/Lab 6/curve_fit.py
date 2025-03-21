# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Amina Hajiyeva"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101303729"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-082"

#==========================================#
# Place your curve_fit function after this line

# import required polynomical functions
import numpy as np
import matplotlib.pyplot as plt

def curve_fit(machine_dict: dict, attribute: str, degree: int) -> str:
    """
    Return the string representation of the equation of the best fit for the average of M_AVG.
    Precondition: N/A.
    >>>curve_fit( [{'CACH': 1, 'M_AVG': 2}, {'CACH': 2, 'M_AVG': 3}, {'CACH': 3, 'M_AVG': 5}], 'CACH', 2)
    'y = 0.5x^2 +  -0.5x + 2.0'
    >>>curve_fit( [{'CACH': 1, 'M_AVG': 2}, {'CACH': 2, 'M_AVG': 3}, {'CACH': 3, 'M_AVG': 5}], 'CACH', 5)
    'y = 0.5x^2 +  -0.5x + 2.0'
    curve_fit( [{'CACH': 5, 'M_AVG': 6}, {'CACH': 2, 'M_AVG': 8}, {'CACH': 4, 'M_AVG': 8}], 'CACH', 2)
    'y = -0.67x^2 +  4.0x + 2.67'
    """
    # dictionary that stores all the values
    all_values = {}
    # variables to hold the averages of the attribute and M_AVG
    average_attribute = 0
    m_avg = 0
    # empty list to hold M_AVG values from the all_values dictionary as well as the lists for the points of each
    m_avg_values = []
    m_avg_points = []
    attribute_avg_points = []
    # empty strings for equation
    equation = "y ="
    variable = ""
    # variables for creating equation
    i = degree
    j = 0
    deg = 0
    count = 0

    # iterate through each element in dictionary
    for machine in machine_dict:
        # collect the values of the desired attribute of each machine in another list
        values_of_attribute = machine[attribute]

        # if the value of the attribute is not in the dictionary, create an empty list for it to later be able to add to that list with the correct M_AVG value
        if values_of_attribute not in all_values:
            all_values[values_of_attribute] = []

        # add the M_AVG value of the attribute to the list
        all_values[values_of_attribute].append(machine['M_AVG'])

    # begin to calculate average of all of the M_AVG by adding all of the values together
    for key in all_values:
        average_attribute += key
        # points will be needed to create equation, so create a new list with the points all together in one single list
        attribute_avg_points.append(key)

    # strip the dictionary into only its values to find the average
    m_avg_values = all_values.values()
    
    # for each value add it to another variable to be able to calculate the average by division
    for value in m_avg_values:
        # since the values() function returns the values in individual lists, make sure the variable m_avg holds the required values
        m_avg += value[0]
        # points will be needed to create equation, so create a new list with the points all together in one single list
        m_avg_points.append(value[0])

    # to determine the final average of the attribute and the M_AVG values, divide the total by the total number of values of the attribute and of M_AVG
    average_attribute = average_attribute / len(all_values)
    m_avg = m_avg / len(m_avg_values)
    
    # if order is higher than interpolating polynomial
    if degree > len(all_values):
        # reassign the degree value as the number of values
        degree = len(all_values) - 1
        coefficients = np.polyfit(attribute_avg_points, m_avg_points, degree)
        
    # create coefficients for the equation
    else:
        coefficients = np.polyfit(attribute_avg_points, m_avg_points, degree)

    # create the equation
    for i in range(0, degree - 1):
        # make sure the first degree is the highest one, and then decrease by one each time
        i = degree + 1
        count += 1
        i -= count
        # add the x^degree to the equation for each value
        variable = " " + \
            str(round(coefficients[j], 2)) + "x^" + str(i) + " + "
        equation += variable
        # increase j to continue iterating through coefficients
        j += 1

    # add last values to equation (last x value and constant)
    equation += " " + str(round(coefficients[-2],2)) + "x + " + str(round(coefficients[-1],2))

    # return the equation
    return equation

# Do NOT include a main script in your submission

