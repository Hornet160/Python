                                   # solution one

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# .................................

#..............................
# print(names)
# length_of_list=len(names)
random_name_index=random.randint(0,len(names)-1)

print(f"{names[random_name_index]} is going to buy the meal today!")

                             #Solution two
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# ...........................

#..........................
# get the total number of items in the list
length_of_list=len(names)
# Generate random numbers between 0 and the last index
random_name_index=random.randint(0,length_of_list-1)
# pick random person from list using random number.
person_to_pay=names[random_name_index]

print(person_to_pay + " is going to buy the meal today!") # string concatination
