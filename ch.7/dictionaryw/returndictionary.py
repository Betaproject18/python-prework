def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings")
    for topping in toppings:
        print("- " + topping)


make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms','green peppers','extra cheese')


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton',field='physics')

print(user_profile)
