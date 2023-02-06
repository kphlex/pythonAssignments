""" 1. Countdown - Create a function that accepts a number as input.
Return a new list that counts down by one, from the number (as the 0th element)
down to 0 (as the last element).
"""
def countDown(input):
    count = []
    for i in range(input, 0 -1, -1):
        count.append(i)
        
    return count
print(countDown(10))

"""2. Print and Return - Create a function that will receive a list with two numbers
Print the first value and return the second value. """

list = [5, 7]

def printAndReturn(list):
    print(list[0])
    return list[1]
printAndReturn(list);

"""3. First Plus Length - Create a function that accepts a list and returns the
sum of the first value in the list plus the list's length. """

listTwo = [12, 7, 4, 33, 2, 9, 14]

def first_plus_length(listTwo):
    sum = listTwo[0] + (len(listTwo))
    print(sum)
    return sum
first_plus_length(listTwo)

"""4. Values Greater than Second - Write a function that accepts a list and creates
a new list containing only the values from the original list that are greater
than its 2nd value. Print how many values this is and return the new list. If the list
has less than 2 elements, have the function return false."""

oldList = [94, 88, 56, 24, 178, 7, 989]

def valuesGreaterSecond(oldList):
    newList = []
    if (len(oldList)) <= 2:
        print("False")
        return "False"
    else:
        for i in oldList:
            if i > oldList[1]:
                newList.append(i)
        print(len(newList))
        return newList

valuesGreaterSecond(oldList)

"""5. This Length, That Value - Write a function that aceepts two ints as parameters:
size and value. The function should create and return a list whose length is
equal to the given size, and whos values are all given the value."""

def lengthAndValue(size, value):
    theList = []
    for i in range(size):
        theList.append(value)
    print(theList)
    return theList

lengthAndValue(10,100)