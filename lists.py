#list declaration
grades = [7.9, 9.7, 8.2]
list1 = [] #declairing an empty list
list2 = list()
list3 = [18, 'mariana', 3.7182, False] #different variable types
list_of_lists = [1, [2, 3, 4]] #list incluiding a list

#list index
print(list3[1])  #print list slot 1
print(list3(-1)) #acesses lists last value

#slice
list4 = [10, 50, 3, 95, 46, 87, 16, 35, 2, 41]
print(list4[0:3]) #prints slots 0 through 3(-1, so 2)
print(list4[0:])  #prints whole list
print(list4[0:9:2]) #prints slots 0-9 skipping two

#for iterations
for element in list4: #prints each element in list4
    print(element)

print('List4 lenght: ', len(list4)) #prints lists lenght

for i in range(len(list4)): 
    print(i) 