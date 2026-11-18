
    
print("welcome to calculator")
def add(x,y):
    answer = x+y
    return answer
def subtract(x,y):
    answer = x-y
    return answer
def multiply(x,y):
    answer = x*y
    return answer
def divide(x,y):
    answer = x/y
    return answer

try:
    
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError:
    print("use numbers only")

operation = input("pick operation- add subtract multiply or divide").lower().strip()

if operation == "add":
    add = add(num1,num2)
    print("answer is", add)
elif operation == "subtract":
    add = subtract(num1,num2)
    print("answer is", add)
elif operation == "multiply":
    add = multiply(num1,num2)
    print("answer is", add)
elif operation == "divide":
    add = divide(num1,num2)
    print("answer is", add)



