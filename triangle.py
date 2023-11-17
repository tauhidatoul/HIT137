#Group Name: Group 10 DAR

# Group Members:
# Tauhidul Islam Atoul - S37797
# Shaikat Barua - S373812
# Dev Rajeshkumar Patel - S374284
# Divyeshkumar Patel - S360946

# 1.a) Ask the user to input three numbers, and check if these three numbers can form a triangle.
#⚫ Need three inputs.

def triangle(a, b, c):
    # For three points to be able to form a triangle, 
    # sum of any two sides need to be grewater than the third side.
    if (a+b>c) and (a+c>b) and (b+c>a):
        return True
    else:
        return False
    
# To Input the lengths of the three sides of the triangle:
a = int(input('Input the length of side a: '))
b = int(input('Input the length of side b: '))
c = int(input('Input the length of side c: '))
    
if triangle(a, b, c):
     print ('The given three lengths can form a triangle.')
else:
     print ('The given three lengths cannot form a triangle')