def cfang(a,b):
    c=a
    if b==0:
        c=1
        return c
    else:
        for i in range(1,int(b)):
            c=c*a
            print(i)
        return c
print(cfang(10,4))