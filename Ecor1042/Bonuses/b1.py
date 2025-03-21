# number 1:

# list of tuple to encode grades of each student
# list of tuples with student id and grade
information_students = [(10, 55), (23, 66.7), (14, 87)]
print(information_students)

# number 2:

# add a student to tuple with grade 57
new_student = (99, 57)  # new student created
information_students.append(new_student)  # add new student to list
print(information_students)

# number 3:

# check is student 38 is in the class
for student in information_students:
    if student[0] == 38:  # if student number is equal to number searched, print true
        print(True)
    else:
        print(False)

# number 4:
    
# check how many students got above 50% in the course
above_50 = 0  # counter of students scoring above 50

for student in information_students:
    if student[1] > 50:  # if student grade is above 50, increase counter by one and then print total
        above_50 += 1
print(above_50)

# number 5:
    
# create sorted version of list, student numbers in ascending order
# for each student, set the lowest number to 0 to then later compare values
for i in range(len(information_students)):
    min_idx = i  # find min
    # if the previous minimum is greater than a student number, switch the minimum value
    for j in range(i + 1, len(information_students)):
        if information_students[min_idx][0] > information_students[j][0]:
            min_idx = j  # create new minimum
    # switch values as required
    information_students[i], information_students[min_idx] = information_students[min_idx], information_students[i]

print(information_students)