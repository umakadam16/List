# Write a program to find the second smallest element in the list.
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
list1.sort()
print("after sorting a list:",list1)
# find the smallest element in the list
smallest=min(list1)
print("smallest element in the list:",smallest)
smallest=list1[1]
print("secound smallest element in the list:",smallest)


