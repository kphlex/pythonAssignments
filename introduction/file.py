
num1 = 42 # Variable Declaration Int
num2 = 2.3 # Variable Declaration Float
boolean = True # Variable Declaration Boolean
string = 'Hello World' # Variable Declaration String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Dic
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dic
fruit = ('blueberry', 'strawberry', 'banana') # List
print(type(fruit)) # Log Statment - type check 
print(pizza_toppings[1]) # log statment - tuple (sausage?)
pizza_toppings.append('Mushrooms')#dic add value
print(person['name']) # dic access value
person['name'] = 'George' # dic change value
person['eye_color'] = 'blue' # dic add value
print(fruit[2]) # list log statment 

if num1 > 45: #conditional
    print("It's greater") # log statement 
else: # conditional
    print("It's lower") # log statement

if len(string) < 5: # conditional
    print("It's a short word!") # log statment
elif len(string) > 15: # conditional 
    print("It's a long word!") # log statment
else: # conditional
    print("Just right!") # log statement

for x in range(5): #For Loop  start / stop
    print(x) # log statement 
for x in range(2,5):# For Loop start 2 / stop 5?
    print(x)
for x in range(2,10,3): # for loop start 2 / stop 10 ?
    print(x)
x = 0
while(x < 5): # while loop - Start 0 / End 5
    print(x) # log statement
    x += 1 # increment 

pizza_toppings.pop() # remove the last value in Dictionary?
pizza_toppings.pop(1) # remove the value at index 1 in dictionary?

print(person) # log statement
person.pop('eye_color') # remove eye_color from Dictionary ?
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional
        continue # continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional
        break # break from loop

def print_hello_ten_times(): # define function
    for num in range(10): # argument (10 is parameter)
        print('Hello') # log statement

print_hello_ten_times() # calling function

def print_hello_x_times(x): # define function
    for num in range(x): # argument (x is parameter)
        print('Hello') # log statement

print_hello_x_times(4) # calling function passing 4 as parameter

def print_hello_x_or_ten_times(x = 10): # define function
    for num in range(x): # argument (x is parameter)
        print('Hello') # log statement

print_hello_x_or_ten_times() # calling function with no parameter?
print_hello_x_or_ten_times(4) # calling function setting 4 as parameter


"""
Bonus section 
comment!
"""

# print(num3) - log statement
# num3 = 72 - variable Declaration - int 
# fruit[0] = 'cranberry' - changing value of index 0
# print(person['favorite_team']) error?
# print(pizza_toppings[7]) error?
#   print(boolean) True
# fruit.append('raspberry') ?
# fruit.pop(1) ?