print("My DSA start from today!!!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name, "! You are", age, "years old.")
""" THIS IS FOCUSED DSA LEARNING..."""
word = "Python"
word = "J" + word[1:]
print(word)
#checking largest number
a=int(input("Enter a Number:"))
b=int(input("Enter a Number:"))
c=int(input("Enter a Number:"))
if a>=b and a>=c:
    print(f"{a} is largest number")
elif b>=a and b>=c:
    print(f"{b} is largest number")
else:
    print(f"{c} is largest number")
#checking postive,negative or zero
num=int(input("Enter a number: "))
if num>0:
    print(f"{num} is a positive number!!")
elif num<0:
    print(f"{num} is a negative number!!")
else:
    print(f"{num} is a zero!!")
#building a simple calculator
num1=int(input("Enter a Number:"))
num2=int(input("Enter a Number:")) 
operation=input("enter the operation you want to perform (+-*/%//): ")
if operation=="+":
    print(f"{num1}+{num2}={num1+num2}") 
elif operation=="-":
    print(f"{num1}-{num2}={num1-num2}")
elif operation=="*":
    print(f"{num1}*{num2}={num1*num2}")   
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"{num1}/{num2}={num1/num2}")
elif operation=="%":
    print(f"{num1}%{num2}={num1%num2}")
elif operation=="//":
    print(f"{num1}//{num2}={num1//num2}")
else:
    print("Invalid operation!!")

#Grade Testerrr!!!
marks=float(input("Enter a marks:"))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")
elif marks>=60 and marks<70:
    print("D")
elif marks<=59 and marks>=0:
    print("Fail")
else:
    print("Invalid marks")
    
#Leap Year Tracker
year=int(input("Enter a Year: "))
if year%400==0 or year%4==0 and year%100!=0:
    print(year,"is a leap year")
else:
    print(year,"is not aleap year")

#Even or odd tracker
num3=int(input("Enter a Number:"))
if num3%2==0:
    print(f"{num3} is a even number")
else:
    print(f"{num3} is odd number")












