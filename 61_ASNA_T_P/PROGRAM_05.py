def ls():
    s1=input("enter the  elements in first list separated by spaces:")
    l1=[int(x) for x in s1.split()]
    s2=input("element the elements in first list separated by spaces:")
    l2=[int(x) for x in s2.split()]
    for i in lp1:
        for j in l2:
            if i==j:
                return True
            return False
result=ls()
print(result)
