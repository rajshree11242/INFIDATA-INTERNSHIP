name=input("enter your name")
age=int(input("enter you age"))
unit=int(input("enter unit consumed"))

cost=0

if(unit<=100):
    print("no charge")
elif(unit>100 and unit<=200):
    cost=(unit-100)*5
    print("electricity bill:",cost)
else:
    cost=(unit-100)*10
    print("electricity bill:",cost)