def factor_of_number(a):
    if(a%b==0):
        return "b is factor of a"
    else:
        return "b is not factor of a"
a=int(input("enter a number"))
b=int(input("enter a number to find whether the number is factor of the number entered"))
res=factor_of_number(a)
print(f"the number{a} is {res}")