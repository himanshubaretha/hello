n = int(input())
nsp=n//2
nst=1
nsp1=-1
for i in range(n):
    for k in range(nsp):
        print("\t",end="")
    for m in range(nst):
        if i!=0:
            print("*\t",end="")
    for j in range(nsp1):
        print("\t",end="")
    for m in range(nst):
        if i!=n-1:
            print("*\t",end="")
    print()
    if i<n//2:
        nsp-=1
        nsp1+=2
    else:
        nsp+=1
        nsp1-=2
    
