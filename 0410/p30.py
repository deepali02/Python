# wap to accept no and print table of that number
num=int(input("enter num"))
res=1
for x in range(1,11):
    res=num * x
    print(num,"*",x,"=",res)
