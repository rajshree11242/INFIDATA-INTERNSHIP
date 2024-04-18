l1=[2,3,4,10,15,4,50]
print("list l1:",l1)

sum=0
avg=0
for i in l1:
    sum=sum+i
print(sum)

avg=sum%len(l1)
print(avg)

