a,b,n = list(map(int,input().split()))
c = "{:.{digit}f}".format(a/b,digit = n+3)
#print(c)
print(c[-4:-1])