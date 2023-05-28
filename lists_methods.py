list1 = [1, 3, 12, 8, 2]
print('before append: ' ,list1)

#append
list1.append(3)
print('after append: ' ,list1)

#insert
list1.insert(2, 10)
print('after insert: ' ,list1)

#extend
list2 = [54, 14, 65, 2, 32, 10]

list1.extend(list2)
print('after extend: ' ,list1)

#pop
list1.pop()
print('after pop: ' ,list1) 
#because it wasn't mentioned the position to be eliminated, it eliminated the last element

list1.pop(0)
print('after pop: ' ,list1)
#eliminated the element in position 0 v 