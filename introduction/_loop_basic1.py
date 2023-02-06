# 1. Basic = Print all ints from 0 - 100. 

for i in range(0, 101):
    print(i)
    
# 2. Multipules of Five - Print all the multiples of 5 for 5 - 1000.

for i in range(5, 1005, 5):
    print(i)

# 3. Counting, the dojo way - Print ints 1 - 100. If divisible by 5, print "Coding"
# If divisible by 10 print "Coding Dojo"

for i in range(1, 100):
    if i % 10 == 0: 
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


# 4. Whoa. That Sucker' Huge - Add odd ints from 0 - 500,000, and print the final sum.
sum = 0
for i in range(0, 500000):
    if i % 2 != 0:
        sum = sum + i
print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 1, -4):
    print(i)

"""6. Flexible Counter - Set three variables. lowNum, highNum, mult. Starting
at lowNum and going through highNum, print only the ints that are a multiple of 
mult. IE lowNum =2, highNum = 9, mult = 3, the loop should print 3,6,9 
(on successive lines)"""

lowNum = 2
highNum = 75
mult = 7

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)