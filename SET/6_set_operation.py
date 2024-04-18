a={1,2,3,4,5}
b={4,5,6,7,8}
print("a|b:",a|b)
print(a.union(b))
#eliminate duplicate elements and merge the set
print(a.intersection(b))
print(a&b)
#print the common elements
print(a.difference(b))
print(a-b)
#print the elements not present in b
print(b.difference(a))
print(b-a)
#print elements not presents in a
print(a.symmetric_difference(b))

print(a^b)
#print the elements excluding the common elements