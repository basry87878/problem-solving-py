n=int (input("n:"))
k=int (input("k:"))
mid=int(n/2)
list1=[]
list2=[]

for i in range(1,n+1):
    if (i%2 != 0):
        list1.append(i)
    else:
        list2.append(i)
        
for i in range(0, mid):   
    list1.append(list2[i])

print(list1[n-1])