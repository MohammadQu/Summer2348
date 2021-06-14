# Mohammad Qureshi
# PSID 1789301
# LAB 2.19

# PART 1
# INPUT NUMBER OF LEMON, WATER, AND NECTAR CUPS AND SERVINGS
print('Enter amount of lemon juice (in cups):')
lemon = int(input())
print('Enter amount of water (in cups):')
water = int(input())
print('Enter amount of agave nectar (in cups):')
nectar = float(input())
print('How many servings does this make?')
serve = int(input())
print()

# OUTPUT USER INPUT
print('Lemonade ingredients - yields', ('{:.2f}'.format(serve)) , 'servings')
print(('{:.2f}'.format(lemon)), 'cup(s) lemon juice')
print(('{:.2f}'.format(water)), 'cup(s) water')
print(('{:.2f}'.format(nectar)), 'cup(s) agave nectar')
print()


# PART 2
# INPUT SERVING SIZE
print('How many servings would you like to make?')
servings = int(input())
print()

# OUTPUT INGREDIENTS BASED ON SERVING INPUT
print('Lemonade ingredients - yields', ('{:.2f}'.format(servings)) , 'servings')
print(('{:.2f}'.format(servings/3)), 'cup(s) lemon juice')
print(('{:.2f}'.format(servings*2.6666666)), 'cup(s) water')
print(('{:.2f}'.format(servings/2.4)), 'cup(s) agave nectar')
print()

# PART 3
# CONVERT CUPS TO GALLONS
print('Lemonade ingredients - yields', ('{:.2f}'.format(servings)) , 'servings')
print(('{:.2f}'.format((servings/3)/16)), 'gallon(s) lemon juice')
print(('{:.2f}'.format((servings*2.6666666)/16)), 'gallon(s) water')
print(('{:.2f}'.format((servings/2.4)/16)), 'gallon(s) agave nectar')

