# Q.1)Create dynamic list where you will ask user to enter 5 elements 
# in it and perform insert new element and delete an element operation on it.

my_list = []
print("Enter 5 elements for the list:")
for i in range(5):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

# Display the initial list
print("\nInitial List:", my_list)
# Insert a new element on list
my_list.insert(2,5)
print("After insert a new element :",my_list)
#  perform delet opretion on list
val=my_list.pop(4)
print("After deleting elemnt in list:",my_list)