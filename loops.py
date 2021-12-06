# #while loop
# number = 0

# while (number <= 10):
#     print (number)
#     number += 1
#     #indentation needed to show whats in the whileloop

# #infinite loop 
# a = 1 
# while a ==1:
#     print ("Welcome to ClubBowa")
#     age = int(input ("how old are you? "))
#     if age >= 21:
#         print ("welcome in")
#     elif age >=18:
#         print ("just a couple more years")
#     else:
#         print ("you need to be 21")
# #use ctrl+D to end infinite loop


# #for loop
# for num in range(10, 20):
#     print (num)

# for letter in "Python":
#     print ("Current Letter: " + letter)

#Nested Loop
lines = int(input("how many lines?" ))
row = 0
while (row < lines):
    col = 0
    while(col < lines):
        print("*", end='')
        col += 1
    row += 1
    print()