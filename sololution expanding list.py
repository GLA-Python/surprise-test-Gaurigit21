def expanding(lst):
    lst2=[]
    for i in range(1,len(lst)):
        g=lst[i]-lst[i-1]
        lst2.append(abs(g))
    n=True
    for j in range(1,len(lst2)):
        if lst2[j]>=lst2[j-1]:
            n=False
            break

    return n

lst=list(map(int,input().split()))
print(expanding(lst))
