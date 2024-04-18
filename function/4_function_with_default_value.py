print("function with default value demo")
def addition (a=5,b=20):
    sum=a+b
    print("add of {0} and {1} is {2} ". format (a,b,sum))


print("addition prgm using function")
n1=int(input("first number"))
n2=int(input("second number"))
addition()

addition(n1,n2)
addition(n1)

print("end of the code")