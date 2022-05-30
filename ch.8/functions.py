#Functions..
# def (Name of function)():
    # (docstring)- comment that describes the function in triple quotes
    # Job for the function - print("Hello")

#calling the function - (name of function)
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#passing information to a function
def greet_user(username):
    """simple greeting"""
    print("Hello " + username.title())

greet_user('jake')

#passing info to a function explained
# def greet_user(parameter/variable EX."username")
    #Definition
    #print("Hello " + username.title())

#greet_user('argument/ EX. 'jake')
#Storing 'jake' in paramter/variable username

#Favorite Book
def fav_book(favorite_book):
    """Favorite book"""
    print("My favorite book is "+ favorite_book.title())
    
fav_book('alice in wonderland')

#Positional arguments
# Need to be in same order the parameters were written

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title()+".")

describe_pet('hamster','harry')

#Keyword Arguments
#Name-Value pair that you pass to a function.

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title()+".")

describe_pet(animal_type='hamster', pet_name='harry')

#Default Value
#If argument for parameter is provided, python uses it,
#if not it uses parameters default value

def describe_pets(pets_name, animal_types='dog'):
    print("\nI have a " + animal_types + ".")
    print("My " + animal_types + "'s name is " + pets_name.title()+".")

describe_pets(pets_name='Willie')

def make_shirt(size, description):
    print("We have t-shirts in multiple sizes, to include "+ size.title())
    print(description.title())
make_shirt('small', "I love python")
# Return Values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name1(first_name, middle_name, last_name):
    """Return a full name, neatly"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name1('john','lee','hooker')
print(musician)

def get_formatted_name2(first_name,last_name,middle_name=""):
    """Full name but middle name is optional"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name2("jimi","hendrix")
print(musician)

musician = get_formatted_name2("john","hooker","lee")
print(musician)

def get_name(first_name, last_name):
    """Return a full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
        print("\nPlease tell me your name:")
        print("(enter 'q' at any time to quit.)")

        f_name = input("First name: ")
        if f_name == 'q' or 'Q':
            break
        l_name = input("Last name: ")
        if l_name == 'q' or 'Q':
            break

        formatted_name = get_name(f_name,l_name)
        print("\nHello, " + formatted_name + "!")
        



