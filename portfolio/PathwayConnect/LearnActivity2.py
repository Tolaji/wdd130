num_cookies = int(input("Enter the number of cookies: "))
num_people = int(input("Enter the number of people: "))
cookies_per_person = num_cookies / num_people
print("Each person will get", cookies_per_person, "cookies.")

"""
Author: Brother Burton

Purpose: Practice using mathematical expressions.
"""

age = int(input("How old are you? "))
next_year_age = age + 1
print(f"On your next birthday, you will be {next_year_age}.")

# Note that we could do the addition right in the display if we wanted:
print(f"On your next birthday, you will be {age + 1}.")

print() # This prints a blank line

cartons = int(input("How many egg cartons do you have? "))
eggs = cartons * 12
print(f"You have {eggs} eggs")

# In the next example, to create a blank line I included \n at the beginning of the string
cookies = int(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))

cookies_per_person = cookies / people

print(f"Each person may have {cookies_per_person} cookies")