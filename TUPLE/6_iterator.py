t1=(2,3,4,565,45,30)
print(t1)

#for i in t1:
 #   print(i)

sum=0
avg=0
for i in t1:
    sum=sum+i
    print(sum)

avg=sum%len(t1)
print(avg)
    