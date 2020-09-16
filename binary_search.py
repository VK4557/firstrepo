def searching(sl,s):
    u=0
    l=s-1
    while u<=l:
        mid=(u+l) // 2
        if num==sl[mid]:
            return mid
        else:
            if num<sl[mid]:
                l=mid-1
            else:
                u=mid+1
    else:
        return False

lst=[]
s=int(input("Enter the size of list: "))
print("Enter the values: ")
for i in range(s):
    a=int(input())
    lst.append(a)
sl=sorted(lst)
print("Sorted list is: ",sl)
num=int(input("Enter the number to want to search: "))
sn=searching(sl,s)
if sn:
    print("Number found at",sn+1)
else:print("Number not found!")
