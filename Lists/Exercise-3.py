#Given a list of integer numbers
numbers = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# Given an integer of number
x = 10
#Set a counter to zero
count = 0
for num in numbers:
    #if the x is equal to the number in the list, add 1 to the counter
    if (num == x):
        count = count + 1
# print out the result
print(numbers)
print ("x=" ,x)
print("output: ", count)
