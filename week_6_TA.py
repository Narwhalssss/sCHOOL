def minus(num1,num2):
    return num1 - num2
def plus(num1,num2):
    return num1 + num2
def times(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2

print("""pick an opperation :
      1.add
      2.minus
      3.substract
      4. multlipication 
      """) 

bruh = "yes"
while bruh == "yes":
    redpill = input('pick your opperation: ')
    num1 = eval(input('enter the first number : '))
    num2 = eval(input('enter the second number : '))
    
    if redpill == "1":
        print(plus(num1,num2))
    elif redpill == "2":
        print(minus(num1,num2))
    elif redpill == "3":
        print(divide(num1,num2))
    elif redpill == "4":
        print(times(num1,num2))
    else:
        print("you can only put a number from 1 to 4 ")
    bruh = input('would you like to run the code again yes/no? ')
else:
    print("The code has stopped")
    
