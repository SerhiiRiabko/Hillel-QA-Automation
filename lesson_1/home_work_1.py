""" 1. Create variables john_salary and marta_salary of some type (floating point).
 Assign the created variables the values ​​ you want. Print the values ​​ of
 both variables to the console using the print method."""
john_salary = 10000.6
marta_salary = 12500.8

print(john_salary)
print(marta_salary)

print("John Salary - " + str(john_salary))
print("Marta Salary - " + str(marta_salary))

'''
2. Create variables john_age and marta_age of integer type. Assign the created variables the values
 ​​ you want. Print the values ​​ of both variables to the console using the print method.
'''
john_age = 28
marta_age = 32

print(john_age)
print(marta_age)

print(f"John age is  + {john_age}")
print(f"Marta age is  + {marta_age}")

'''
3. Create string type variables john_name and marta_name. Assign the created variables
the values ​​ you want. Print the values ​​ of both variables to the console using
the print method.
'''
john_name = "Smith"
marta_name = "Nous"

print(john_name)
print(marta_name)

print("John's surname is " + john_name)
print("Marta's surname is " + marta_name)

'''
4. Create boolean variables john_gender and marta_gender. Let john be false and Marta be true.
 Print the values ​​of both variables to the console using the print method.
'''
john_gender = False
marta_gender = True

print(john_gender)
print(marta_gender)

if john_gender is False:
    print("John's gender is Man")
if marta_gender is True:
    print("Marta's gender is Woman")
'''
5. Create variables john_friends and marta_friends. Assign lists to variables.
Each list must contain the names of friends.
John has his list of friends and Martha has hers. Friends (friend's name) can be the usual strings
 "James", "Peter", etc.
 '''
john_friends = ["Fred", "Garry", "Shoen", "Ron", "Germiona", "Hagreed"]
marta_friends = ["Lili", "Valery", "Germiona", "Palomna", "Hagreed"]

'''
6. Create a list with people's names, some names should be repeated in it.
 Turn a list of duplicate names into a list of unique names using sets.
'''
peoples_name = ['Fred', "Ron", "Gleb", "Turs", "Ron", "Fred"]
set_people_name = set(peoples_name)
print(set_people_name)

'''
7. Create 2 tuple variables. The tuple must consist of 2 floating point numbers.
The first value of the tuple is the latitude where you live, and the second value is the 
longitude where you live.
'''
my_place = (48.06, 34.0)
latitude, longitude = my_place

'''
8. Create 2 variables john, marta. Variables must be dictionaries with keys:
 full_name, age, salary, gender, friends, coordinates.

Structure requirements:

Full_name - full name

Age - age

Salary - salary

Gender - the gender of the person (use boolean)

Friends - list of friends from task 6

Coordinates - longitude and latitude from task 7

Print the key and value for john and martha to console:
“key => value” where key is the key of the dictionary pair and
value is the value of the dictionary pair.
'''
john = {"Full_name": "John Smith", "Age": john_age, "Salary": john_salary, "Gender": "Man", "Friends": john_friends,
        "Coordinates": my_place}
marta = {"Full_name": "Marta Nos", "Age": marta_age, "Salary": marta_salary, "Gender": "Woman",
         "Friends": marta_friends,
         "Coordinates": my_place}
for key, value in john.items():
    print(str(key) + "-" + str(value))
for key, value in marta.items():
    print(str(key) + "-" + str(value))

'''
*challenge:

Task from point 8. Instead of strings in the list of friends, there should be the same
 dictionaries as john and marta. Create 2 friends each for John and Martha.
 Print John and Martha's fields to the console. '''
'''
john = {"Full_name": "John Smith", "Age": john_age, "Salary": john_salary, "Gender": "Man", "Friends": john_friends,
        "Coordinates": my_place}
marta = {"Full_name": "Marta Nos", "Age": marta_age, "Salary": marta_salary, "Gender": "Woman",
         "Friends": marta_friends,
         "Coordinates": my_place}
j_friend = (john["Friends"])
m_friends = (marta["Friends"])
print(list(set(j_friend) & set(m_friends)))
Leave this code as example for another situation
'''

marta_f = {"friend Marta 1": "Suzzy", "friend Marta 2": "Angela"}
john_f = {"friend John 1": "Gustav", "friend John 2": "Faust"}

for key, value in john_f.items():
    print(str(key) + "-" + str(value))
for key, value in marta_f.items():
    print(str(key) + "-" + str(value))
