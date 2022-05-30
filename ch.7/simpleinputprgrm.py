prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            continue

    print(current_number)

prompt1 = input("What toppings would you like on yur pizza?")
prompt1 += ("\nWhen you are finished, enter 'quit'.")
messages = ""
while messages != 'quit':
    messages = input(prompt1)
    print(messages)



# unverified users to verified users list
#start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users
#move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

#display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    

