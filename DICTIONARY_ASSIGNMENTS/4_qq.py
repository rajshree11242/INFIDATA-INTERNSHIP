a={1:24,2:34,3:44}
b={4:54,5:64}
def replace(a,b):
    for i in b.keys():
        a=replace(a,b)
        print(a)
