#dictionary values
# stored in key and value types.


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['points'])
# assigning a variable to the value of a dictionary
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
# adding new key-values to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# starting  with a blank dictionary
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = 15
print(alien_1)
#modifying values in a dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#removing key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah':  'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is "+
    favorite_languages['sarah'].title()+".")

jacob = {'age':22,'city':'salem','last_name':'mifflin'}
print(jacob)
print(jacob['age'])
print(jacob['city'])
print(jacob['last_name'])

favorite_numbers = {'janice': 25, 'michael': 15, 'alice': 4}
print(favorite_numbers['alice'])
print(favorite_numbers['michael'])
print(favorite_numbers['janice'])

glossary = {'sort': "sorts the list its attached to",'upper':
    'prints the statement its attached to in all uppercase'}

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title()) 

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title())

print(" The following languages have been mentioned")
for language in set(favorite_languages.values()):
    print(language.title())


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


#make an empty list for storing aliens
aliens = []

#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Show first fivve aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many number of aliens have been created
print("Total number of aliens: " + str(len(aliens)))

#changing a few aliens in the fleet to something else
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:3]:
    print(alien)


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'parts',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

