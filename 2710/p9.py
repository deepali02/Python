#program to accept age and print
# whether it child , adult or old
age=int(input("enter age"))
if age<18:
    print("you are child")
elif age>=18 and age<60 :
    print("you are adult")
elif age>60 and age<100:
    print("your are old")
else:
    print("Age is not valid")
