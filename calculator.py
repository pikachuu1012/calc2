"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


# Replace this with your code
while True: 
    prompt = input("put in a artithmetic operation and 2 numbers:  ")
    #list of prompts
    l = prompt.split(" ")

    newFunc = l[0] 
    print("the list l: ", l)
    print("new Func is: ", newFunc)
    if newFunc == "q":
        print("you quit the calculator! Bye! ")
        break
    
    num1 = int(l[1])
    
    if len(l) > 2:
        num2 = int(l[2])
    if newFunc == "add":
        print(add(num1, num2))
    if newFunc == "subtract":
        print(subtract(num1, num2))
    if newFunc == "multiply":
        print(multiply(num1, num2))
    if newFunc == "divide":
        print(divide(num1, num2))
    if newFunc == "power":
        print(power(num1, num2))
    if newFunc == "mod":
        print(mod(num1, num2))

    if newFunc == "square":
        print(square(num1))
    if newFunc == "cube":
        print(cube(num1))



    
