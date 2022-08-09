# creation of list
myList = [1, 2, 3, 4]
print("Original List: ")
print(myList)

# insertion in a list
myList.append(5)
myList.insert(6, 7)
myList.insert(19, 8)
print("After Insertion:")
print(myList)

# deletion in a list
myList.remove(4)
print("After Deletion:")
print(myList)

# merging another list in a given list
newList = [14, 15, 'Python', 'Java' , 'Kotlin']
print("List 1:")
print(myList)
print("List 2:")
print(newList)
print("Merge two list:")
print(myList + newList)