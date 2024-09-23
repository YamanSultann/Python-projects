lst = [4,5,1,2,9,7,10,8]
print("Original list =", lst)

count = 0

for i in lst:
    count += i

avg = count/len(lst)

print("Sum of list =", count)
print("Average of list =",avg)

lst.sort()

print("Smallest in the list is: ",lst[0])
print("Largest in the list is: ",lst[-1])