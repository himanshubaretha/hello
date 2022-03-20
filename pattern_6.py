n=int(input())
nst=n//2+1
nsp=1
for i in range(n):
    for j in range(nst):
        print("*\t",end="")
    for k in range(nsp):
        print("\t",end="")
    for j in range(nst):
        print("*\t",end="")
    print()
    if i<n//2:
        nst-=1
        nsp+=2
    else:
        nsp-=2
        nst+=1    
    