def adding(A,b):
    return A+b 
def subtract(A,b):
    return A-b 
def multiply(A,b):
    return A*b 
def divide(A,b):
    return A/b 
print("what oppration you want")
print("a=adding")
print("b=subtraction")
print("c=multiplication")
print("d=division")
choise=str(input("Enter your choise "))
x=int(input("enter the first number "))
y=int(input("enter the second number "))
if choise=="a":
    print(adding(x,y))
elif choise=="b":
    print(subtract(x,y))
elif choise=="c":
    print(multiply(x,y))
elif choise=="d":
    print(divide(x,y))
else:
    print("you have entered a invalid option")