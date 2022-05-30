#Creating a list
#index=   0          1           2        3     4
bike = ['trek','specialized','mongoose','dk','hurley']
print(bike)

#Lists are ordered collections, therefore you can access
#  any part of the list by telling Pyhton the position or index

print(bike[0].title())

#you can also print multiple things from a list using a :

print(bike[0:4])


#concatenation with lists(adding strings with an indexed position from a list.)
print("My first bike was made by " + bike[3].upper() + "!")


#Copying lists

my_foods = ['pizza','ice cream','chinese',]
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)


#editing ones list but not the other to prove they are two seperate lists
my_foods.append('chicken')
print(my_foods)
print(friend_foods)



