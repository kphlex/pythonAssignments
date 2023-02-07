"""1. Update the Values in Dictionaries and Lists"""

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15.
x[1][0]= 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0])

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# Change the value 20 in z to 30.
z[0]['y'] = 30
print(z)




"""2. Iterate Through a List of Dictionaries -
Create a function that loops through each dictionary in the list and prints
each key and the associated value."""
# Bonus challenge completed
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(students):
    for i in range(len(students)):
        print("first_name - {}, last_name - {}".format(students[i]['first_name'], students[i]['last_name']))
    
iterateDictionary(students)




"""3. Get Values From a List of Dictionaries -
Create a function that, given a list of dictionaries and a key name, the function
prints the value stored in that key for each dictionary."""

def iterateDictionary2(key_name, students):
    for i in range(len(students)):
        if key_name == 'first_name':
            print(students[i]['first_name'])
        elif key_name == 'last_name':
            print(students[i]['last_name'])
        else:
            print("Not a valid key, ninja.")
        
iterateDictionary2('first_name', students)




"""4. Iterate Through a Dictionary with List Values -
Create a function that given a dictionary whose values are all lists, prints
the name of each key along with the size of its list, and then prints the
associated values within each key's list. """

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for keys, val in dojo.items():
        print("\n",len(val), keys.upper())
        for i in range(len(val)):
            print(val[i])
    
printInfo(dojo)