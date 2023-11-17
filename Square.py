#Group Name: Group 10 DAR

# Group Members:
# Tauhidul Islam Atoul - S37797
# Shaikat Barua - S373812
# Dev Rajeshkumar Patel - S374284
# Divyeshkumar Patel - S360946

# 1.b) Write a python program to solve the following problem.
#Ask users to input one number, the number will be the size of a square. Using the print function to draw this square.
#⚫Need input size.
#⚫The output will be a single square created by the print function

square = int(input('Input the size of the square: '))
space = square-2 #To add the spaces in the middle of the square.
print ("* "*square) #Print the '*' on Row1
for _ in range(space):
    print ("* "+ "  "*(space) + "* ") #Print the '*   *' on Row2 - Row n-1.
print ("* "*square) #Print the '*' on bottom Row.