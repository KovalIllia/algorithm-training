"""1. Perform logical bitwise operations "AND", "OR", etc. on the numbers 5 and 6.
Perform a bitwise shift of the number 5 to the right and left by two digits."""
import random

# a = 5
# print(f"{a}={bin(a)}")
# b = 6
# print(f"{b}={bin(b)}")
# print(f"{a} and {b} = {a & b} {bin(a & b)}")
# print(f"{a} or {b} = {a | b} {bin(a | b)}")
# print(f"{a} xor {b} = {a ^ b} {bin(a ^ b)}")
# print(f"{a} >> 2 = {a >> 2} {bin(a >> 2)}")
# print(f"{a} << 2 = {a << 2} {bin(a << 2)}")
#




"""2. Given the coordinates of two points entered by the user, 
derive the equation of a line of the form y = kx + b passing through these points."""
# print("enter the coordinates of the point A (x1,y1): ")
# x1 = float(input('x1= '))
# y1 = float(input('y1= '))
# print("enter the coordinates of the point B (x2,y2): ")
# x2 = float(input('x2= '))
# y2 = float(input('y2= '))
# print("the equation of a straight line of the form y = kx + b passing through these points. ")
# if x1 == x2:
#     print(f"x={x1:.2f}")
# else:
#     k = (y1 - y2) / (x1 - x2)
#     b = y2 - k * x2
#     print(f"y={k:.2f} * x + {b:.2f} ")






"""3. Write a program that generates, within user-specified boundaries:
a. a random integer,
b. a random real number,
c. a random symbol.
For each of the three cases, the user specifies their own range boundaries. 
For example, if you want a random symbol from 'a' to 'f', then enter these characters. 
The program should display any alphabetical character from 'a' to 'f', inclusive."""
# num_start=input("Start diapazon: ")
# num_end=input("End of diapazon: ")
# choise=input('Enter the action number:\n1. random integer\n'
#              '2.random real number\n3. random character.\n')
# if choise == '1':
#     print("random integer")
#     num_start=int(num_start)
#     num_end=int(num_end)
#     result=random.randint(num_start,num_end)
#
# elif choise == '2':
#     print("random real number")
#     num_start=float(num_start)
#     num_end = float(num_end)
#     result = random.uniform(num_start, num_end)
#
# elif choise == '3':
#     print("random character")
#     num_start=ord(num_start)
#     num_end = ord(num_end)
#     result = chr(random.randint(num_start, num_end))
#
# else:
#     result="Unknown action"
# print(result)
#






"""4. The user enters two letters. Determine where in the alphabet they appear and how many letters are between them."""
# first_value=input("Enter the first value: ")
# second_value=input("Enter the second value: ")
# first_value=ord(first_value)-ord('a')+1
# second_value=ord(second_value)-ord('a')+1
# print(f"ordinal number of the 1st letter: {first_value}, second: {second_value}")
# print(f"number of letters between the entered: {abs(first_value-second_value)-1}")




"""5. The user enters the number of a letter in the alphabet. Determine which letter it is."""
# num=int(input("letter number in the alphabet: "))
# num=ord('a')+num-1
# print(f"this letter: {chr(num)}")




"""6. Given the lengths of three segments entered by the user, determine the possibility of a triangle formed by these segments. 
If such a triangle exists, determine whether it is scalene, isosceles, or equilateral."""
# a=int(input("a= "))
# b=int(input("b= "))
# c=int(input("c= "))
#
# if a+b<=c or a+c<=b or b+c<=a:
#     print("the triangle does not exist")
# if a!=b or a!=c or b!=c:
#     print("triangle with different sides")
# if a==b==c:
#     print("triangle with equal sides")
# else:
#     print("triangle with equal hips")




"""7. Determine whether the year entered by the user is a leap year or not."""
# year=int(input("enter the year in yyyy format: "))
#
# #Example 1
# if year %4 !=0:
#     print("normal year")
# elif year%100==0:
#     if year %400==0:
#         print("intercalary")
#     else:
#         print("normal")
# else:
#     print("intercalary")
#
#
# #Example 2
# if year %4 != 0 or (year%100==0 and year % 400 != 0):
#     print("normal")
# else:
#     print("intercalary")


"""8. Given three different numbers, find the middle one (larger than one but smaller than the other)."""
# a=int(input("1-st: "))
# b=int(input("2-nd: "))
# c=int(input("3-d: "))
#
# if b <a< c or c <a< b:
#     print(f"average num is: {a}")
# if a <b< c or c <b< a:
#     print(f"average num is: {b}")
# else:
#     print(f"average num is: {c}")