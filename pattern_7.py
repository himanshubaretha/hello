n=int(input())
nst=1
nsp=0
for i in range(n):
    for j in range(nsp):
        print("\t",end="")
    for k in range(nst):
        print("*\t",end="")
    print()
    nsp+=1
    