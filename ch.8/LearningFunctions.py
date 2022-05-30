# def NAME_OF_FUNCTION(PARAMETERS):
    # what it does

def hello(name, age):
    print(f"Hello {name} you are {age}")

hello("Jake",22)

def say_hello(name, age):
    print(f"Hello {name} you are {age} years old.")

def say_goodbye():
    print("Goodbye!")

def greet_back(feeling):
    if feeling == "good":
        print("Awesome I feel good too")
    elif feeling == "bad":
        print("Im so sorry")
    elif feeling == "Stressed":
        print("Coding can be hard to learn")
    else:
        print("Well, have a good day!")

#Driver Code
while True:
    response = input("What do you want to do? say hello [H] say goodbye [G] talk to me [T] quit [Q]")
    if response.lower() == 'q':
        say_goodbye()
        break
    elif response.lower() == 'h':
       name = input("What is your name? ")
       age = input("What is your age? ")
       say_hello(name, age)
    elif response.lower() == 'g':
        say_goodbye()
    elif response.lower() == 't':
        feeling = input("How are you today? ")
        greet_back(feeling)
    else:
        print("Invalid")
        