# WAP to display the sum of first n numbers
n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
    print("The sum of first",n,"numbers is :",sum)
