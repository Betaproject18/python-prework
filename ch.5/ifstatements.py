cars = ['audi','bmw','mercedes-benz','chevrolet']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
            print(car.title())


#conditional sets- 'if' statements that rely on true or false 

car = 'bmw'
if car == 'bmw':
    print(car)
    
# messing with case sensitivity while checking for equality
# bmw would print no matter what because car. lower is equal to bmw

car = 'BMW'
car.lower() == 'bmw'
print(car)

# Determining whether two values are not equal, combining an exclamation 
#point and equal sign,(exclamation point means not)

requested_topping = 'mushrooms'
# if topping wanted isnt anchovies, print hold the anchovies
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Testing inequality with numbers is basically the same
min_age = 17
if min_age < 18:
    print("Too young")

# Checking multiple conditions with the and or if statement

age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("Congrats")
else:
    print("Sorry, Try Again...")

# To improve readability use parantheses

age_0 = 22
age_1 = 25
if (age_0 >= 21) and (age_1 >= 21):
    print("Congrats")
else:
    print("Sorry, Try Again...")

#using 'or' to check multiple conditions

age1 = 26
age2 = 25
if age1 >= 27 or age2 <= 24:
    print("Congrats, youre in the age bracket!")
else:
        print("Sorry, you didnt make the cutoff.")

# Seeing if a value is in a  list with the 'in' feature
usernames = ['mickey','bongo','drums28']
username = 'mickey'

if username in usernames:
    print("Congrats")
else:
        print("welcome")

#Boolean expressions - Just another name for a conditional test
# A Boolean value is either true or false
# They are often used to keep track of certain conditions like if a game is running

car = 'subaru'
print("Is car == 'subaru'?  I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')











