n=int(input())
nsp=n//2
nst=1
for i in range(n):
    for j in range(nsp):
        print("\t",end="")
    for k in range(nst):
        print("*\t",end="")
    print()
    if i<n//2:
        nsp-=1
        nst+=2
    else:
        nsp+=1
        nst-=2