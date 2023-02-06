# 1. TASK: print "Hello World"

print ("Hello World")

# 2.  print "Hello Noelle!" witht he name in a variable

name = "Cam"
print ("Hello", name,"!") # with a comma
print ("Hello" + " " + name + "!") # with a +

# 3. print "Hello 42!" with the numnber in a variable

name = 8
print ("Hello" , name, "!") # with a comma
print ("Hello" + " " + str(name) + "!") # with a +

# 4. print "I love to eat sushi and pizza!" with food in variables

fav_food1 = "sushi"
fav_food2 = "pizza"
print ("I love to eat {} and {}!".format(fav_food1, fav_food2)) # with .format()
print (f"I love to eat {fav_food1} and {fav_food2}!") # with an f string