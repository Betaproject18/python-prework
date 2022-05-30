# to add and remove things from lists,
# insert , append(to the back of the list) , pop() method , del method, remove method, and modifying them based
#on index
alist = [1,2,3,4,5,6,7,8,9,0]
print(alist)
alist.insert(0, 'Start')
print(alist)

#append
alist.append('End')
print(alist)
#pop method removes the last item on the list, remember popping the top item off a tower
#first, assign a value to the popped items to call them when needed.
popped = alist.pop()
print("The last item on the list that was popped is " + popped + "!")

# Popping items from any position or index of a list

popped_again = alist.pop(2)

print(alist)
print(popped_again)

# deleting things from a list using the del method
alist = [1,2,3,4,5,6,7,8,9,0]
del alist[0]
print(alist)

#deleting things from the list using the remove statement

alist.remove(3)
print(alist)

#Modifying a list(interchanging items in the list)

alist[1] = 15
print(alist)



