# wap to accept a no and print the factorial of that no using while loop
num=int(input("enter num"))
fact = 1
while num > 0:
    fact = num * fact
    print( "Factorial = " , fact)
    num = num -1
