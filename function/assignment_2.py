def even_or_odd(a):
    if(a%2==0):
        return "even"
    else:
        return "odd"
a=int(input("enter the number"))
res=even_or_odd(a)
print(f"the number{a} is {res}")
