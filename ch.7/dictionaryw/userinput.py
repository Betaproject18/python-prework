from http.client import responses


responses = {}

#setting a flag to indicate that polling is active
polling_active = True

while polling_active:
    #prompt for persons name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #store the response in the dicitonary
    responses[name] = response

    #find out if anyone else is going to take the poll

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    #polling is complete.Show the results.
print("\n--- Poll Results ---")
for name, response in response.items():
    print(name + " Would like to climb " + response + ".")
    