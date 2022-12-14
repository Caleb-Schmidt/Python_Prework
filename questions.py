# Question 1
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of the code has been defined as below.
def hello_name(user_name):
    print("Hello " + user_name + "!")

hello_name("Caleb")

# Question 2
# Write a python function, 
# first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    odds = [odd for odd in range(1,100,2)]
    print(odds)

first_odds()

# Question 3
# Please write a Python function, 
# max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max_items = len(a_list)
    print(max_items)

max_num_in_list([2, 4, 5, 1, 3])

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            print("This is a leap year.")
        else:
            if a_year % 400 == 0:
                print("This is a leap year.")
            else:
                print("This is not a leap year.")
    else:
        print("this is not a leap year.")

is_leap_year(2022)

# Question 5
# Write a function to check to see if all numbers in list 
# are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    first_num = a_list[0]
    last_num = a_list[-1]
    if first_num == last_num - len(a_list) + 1:
        print(True)
    else:
        print(False)
    

is_consecutive([1,2,3,4,5])