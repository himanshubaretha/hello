n=int(input())
nst=1
nsp=n-1
for i in range(n):
    for k in range(nsp):
        print("\t",end="")
    for j in range(nst):
        print("*\t",end="")
    print()
    nsp-=1