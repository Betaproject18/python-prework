# The while loop
#While boolean or boolean exp:
    #code block
    #To run while
    #Condition is true

# You must be over 5 feet to ride
while True:
    response = input("What do you want to do today? Say hi [h], say goodbye [g] or quit [q] ")
    if response.lower() == "h":
        print("Hello")
    elif response.lower() == "g":
        print("Goodbye")
    elif response.lower()=="q":
        break
    else:
        print("invalid option")
