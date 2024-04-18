y=int(input("enter the cost price of the bike"))
if(y>100000):
    print("15% tax on the bike")
elif(y>50000 and y<=100000):
    print("10% tax on the bike")
else:
    print("5% tax on the bike")
print("end of the code")