n=int(input("Enter the number of lines: "))
lis=[1,1]
for i in range(1,n+1):
    print((n-i)*" ", end = "")
    lislin=[1]
    if i==1:
        print(1)
        continue
    elif i==2:
        print("1 1")
        continue
    print(1,end=" ")
    for j in range(i-2):
        lislin.append(lis[j] + lis[j+1])
        print(lis[j] + lis[j+1], end=" ")
    print(1)
    lislin.append(1)
    lis=lislin
