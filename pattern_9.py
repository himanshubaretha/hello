n=int(input())
nsp=0
nst=1
nsp1=n//2+1
for i in range(n):
    for j in range(nsp):
        print("\t",end="")
    for k in range(nst):
        print("*\t",end="")
    for l in range(nsp1):
        print("\t",end="")
    for k in range(nst):
        if i!=n//2:
            print("*\t",end="")
    print()
    if i<n//2:
        nsp+=1
        nsp1-=2
    else:
        nsp-=1
        nsp1+=2