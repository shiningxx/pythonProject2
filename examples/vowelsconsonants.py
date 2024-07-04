str=input("enter the string")
count=0
j=0
for i in str :
    if i in ('a','e','i','o','u'):
        count=count+1
    else:
        j=j+1
print(count, j)
