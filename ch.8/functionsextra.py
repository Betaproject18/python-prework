def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#moving things between lists without a function
#start with some designs that need to be printed
def print_models(unprinted_designs, completed_models):
#simulate printing each desgin, until none are left.
# Move each design to completed_models after printing.
    while unprinted_designs:
        current_design = unprinted_designs.pop()

    #simulate creating a 3d print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

def show_completed_models(completed_models):

# Display all completed models.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedran']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
