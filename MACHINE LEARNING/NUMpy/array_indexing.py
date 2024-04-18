import numpy as np
a=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])

print(a)

s1=a[:2,:3]
print(s1)

s2=a[:2,::2]
print(s2)
#startrow:endrow:step - row range
#start col:end col:step - col range

