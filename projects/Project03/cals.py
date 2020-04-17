# List a file to screen

# List the weights, or foods eaten for a day. List calories by calculation.
# cals list eaten <date>
# cals list weights

# List the dates for which we have calorie counts
# cals list dates

# List the calorie data itself.
# cals list foods

# A generic k-v lookup procedure

# lookup a) calories for a type of food b) weight for a day. Today if missing.
# cals lookup calories <food>
# cals lookup weight <date>

# Print the total calories for just a given day. Today if missing.
# cals total <date>

# Create and initialise new user
# cals newuser <name>

# Add data for today - food and grams
# cals eaten <user> <food> <grams>

# Main program. Read args and dispatch.

if len(sys.argv) > 1
    cmd = sys.argv(1)
    if cmd == 'list'
       #eaten <date>
       #weights
       #dates
       #foods
    elif cmd == 'lookup'
       #calories
       #weight
    elif cmd == 'total'
       #<date>
    elif cmd == 'newuser'
       #<name>
    elif cmd == 'eaten'
       #<user> <food> <grams>
    
