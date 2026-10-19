"""
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
"""

print("Day 2: 30 Days of python programming")
first_name= "Pelumi"
last_name ="Adewale"
full_name = first_name +" " + last_name
age = 19
year = 2007
is_married = False
is_true = True

ranking, level, grade = 30, 300, "first class"

print(ranking)
print(type(first_name))
print(len(first_name))
print(len(last_name))

if len(first_name)< len(last_name):
    print("Last name is longer than first name")
elif len(first_name) == len(last_name):
     print("Both have equal length")
else:
    print("First name is longer")

num_one, num_two = 2, 1
total = num_one + num_two
print("total is: ", total)
modulus =   num_two % num_one
print(modulus)