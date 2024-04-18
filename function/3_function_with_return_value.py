print("function with return value demo")
def addition (a,b):
    sun=a+b
    return sum

print("addition prgm using functionn")
n1=int(input(" first number"))
n2=int(input(" second number"))
res=addition(n1,n2)
print("add of {0} and {1} is {2} ". format (n1,n2,res))
print(" add of {0} and {!} is {2}". format (n1,n2,addition(n1,n2)))
print("end of the code")

