# Task 1
# Given the following three scenarios, choose the best data structure 
# (between a dictionary, set, or tuple) to efficiently store the data.
# Each scenario ties directly to one data structure.
# Each data structure will be used only once.
# You will need to determine which data structure is best for which
# scenario, and then implement the data structure in Python.

# 1) Store the months of the year as strings.
# Determine the month in the data structure in which National Pi Day exists and print that month to the console. 
# a) HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.
months_of_year = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
pi = 3.14
#print(int(pi))
#print(pi)
#print(len(months_of_year))
#print(len(months_of_year[int(pi)]))
#print(months_of_year[pi])
#print(months_of_year[int(pi)])
print()
print(months_of_year[int(pi)-1]) #need the - 1 in order to acount for the 0 index in the tuple
print()

# 2)Store five fruits or vegetables.
# a) Add two of your favorite fruits and two of your favorite vegetables to the collection.
# b) Iterate over the collection and print each one to the console. 


# 3)Store information about a user profile. Use literal string interpolation to print the user’s profile information to the console. The profile should consist of the following information:
# a) First Name
# b) Last Name
# c) Email Address
# d) Phone Number


# Task 2
# Use a list to store the dictionary of your immediate family members, with each index of the list storing its own dictionary. Dictionary should contain the following keys:
# a) First name
# b) Last name
# c) Relation to you