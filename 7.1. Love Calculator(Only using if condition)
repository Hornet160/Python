
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



score1=0
score2=0
person_one=name1.lower()
person_two=name2.lower()
#for true(person one)

if person_one.__contains__("t"):
    score1+=person_one.count("t")
if person_one.__contains__('r'):
    score1+=person_one.count("r")
if person_one.__contains__('u'):
    score1+=person_one.count("u")
if person_one.__contains__("e"):
    score1+=person_one.count("e")
#For true(person two)

if person_two.__contains__("t"):
    score1 += person_two.count("t")
if person_two.__contains__("r"):
    score1 += person_two.count("r")
if person_two.__contains__("u"):
    score1 += person_two.count("u")
if person_two.__contains__("e"):
    score1 += person_two.count("e")

#For love(person one)
if person_one.__contains__("l"):
    score2+= person_one.count("l")
if person_one.__contains__("o"):
    score2 += person_one.count("o")
if person_one.__contains__("v"):
    score2 += person_one.count("v")
if person_one.__contains__("e"):
    score2 += person_one.count("e")

#For love(person two)
if person_two.__contains__("l"):
    score2 += person_two.count("l")
if person_two.__contains__("o"):
    score2 += person_two.count("o")
if person_two.__contains__("v"):
    score2 += person_two.count("v")
if person_two.__contains__("e"):
    score2 += person_two.count("e")
total=str(score1)+str(score2)   #Converting int to string as instructed in the problem
total_int=int(total) # converting str to int as instructed in the problem
print(total_int)
if total_int<10 or total_int>90:
    print(f"Your score is {total_int},you go together like coke and mentos")
elif total_int>=40 and total_int<=50:
    print(f"Your score is {total_int},you are alright together")
else:
    print(f"Your score is {total_int}")
