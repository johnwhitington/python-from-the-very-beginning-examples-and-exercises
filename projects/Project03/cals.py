import sys
# List a file to screen
def table_of_file(filename): pass

# List the weights, or foods eaten for a day. List calories by calculation.
# cals list eaten <date>
# cals list weights
def list_eaten(date): pass
def list_weights(): pass
    
# List the dates for which we have calorie counts
# cals list dates
def list_dates(): pass

# List the calorie data itself.
# cals list foods
def list_foods(): pass

# A generic k-v lookup procedure
def table_lookup(k): pass

# lookup a) calories for a type of food b) weight for a day. Today if missing.
# cals lookup calories <food>
# cals lookup weight <date>
def lookup_calories(food): pass
def lookup_weight(date): pass

# Print the total calories for just a given day. Today if missing.
# cals total <date>
def total_date(date): pass

# Create and initialise new user
# cals newuser <name>
def new_user(name):  pass

# Add data for today - food and grams
# cals eaten <user> <food> <grams>
def eaten(user, food, grams): pass

# Main program. Read args and dispatch.

if len(sys.argv) > 1:
    cmd = sys.argv[1]
    if cmd == 'list':
        if len(sys.argv) > 2 and sys.argv[2] == 'eaten':
            list_eaten(sys.argv[3])
        else:
            if sys.argv[2] == 'weights':
                list_weights()
            elif sys.argv[2] == 'dates':
                list_dates()
            elif sys.argv[2] == 'foods':
                list_foods()
    elif cmd == 'lookup':
        if len(sys.argv) > 2:
            if sys.argv[2] == 'calories':
                lookup_calories(sys.argv[3])
            elif sys.argv[2] == 'weight':
                lookup_weight(sys.argv[3])
    elif cmd == 'total':
        if len(sys.argv) > 2:
            total_date(sys.argv[3])
    elif cmd == 'newuser':
        if len(sys.argv) > 2:
            new_user(sys.argv[3])
    elif cmd == 'eaten':
        if len(sys.argv) > 4:
            eaten(sys.argv[3], sys.argv[4], sys.argv[5])
