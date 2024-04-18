def max(a,b,c):
    max1=max(a,b)
    max2=max(max1,c)
    return max2
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
print("maximum of the three number ",max(a,b,c))

