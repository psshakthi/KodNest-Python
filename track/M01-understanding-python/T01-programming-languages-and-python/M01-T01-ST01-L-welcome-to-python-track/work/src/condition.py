from _typeshed.importlib import PathEntryFinderProtocol
print("----if statemet----")
# Write a program to check whether a person is eligible to vote. if the age is 18 or above, print "Eligible to vote".
age = 32
if(age >= 18):
    print("Eligible to vote")

#Write a program to check whether a person is eligible yo vote. if the age is 18 or above,print "Eligible to vote", else print"not .
age = 14
if(age >= 18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")

print("---nested if statment---")
# Write a program to check whether you are free tonight.
# if you are free, check whether your friends are available. print"GO out for party"
free_tonight = False
friends_avaliable = False
if free_tonight:
    if friends_avaliable:
        print("GO out for party")
    else:
        print("Stay at home and watch movie")
else:
    print("you are not free tonight")
# match-case with multiple casses
#Write a python program that accept a month 3|4|5->Summer and 6|7|8->Rainy 9|10|11|12->autumn |1|2->spring



#update the attempt and find the data type
attempt = 1
print(attempt)
attempt = 3.2
print(attempt)
print(type(attempt))
