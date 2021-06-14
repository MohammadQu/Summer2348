# Mohammad Qureshi
# PSID 1789301
# LAB 3.19


import math
# PART 1
# INPUT HEIGHT/ WIDTH AND CALCULATE AREA
print('Enter wall height (feet):')
height = int(input())
print('Enter wall width (feet):')
width = int(input())
area = height * width
print('Wall area:', area, 'square feet')


# PART 2
#CALCULATE PAINT NEEDED
paint = ('{:.2f}'.format(area / 350))
print('Paint needed:', paint, 'gallons')


# PART 3
# CALCULATE NUM. OF CANS
cans = float(paint)
print('Cans needed:', math.ceil(cans), 'can(s)')
print()

# PART 4
# CREATE A DICTIONARY WITH PAINT AND PRICES
thisdict = {
  "red": "$35",
  "blue": "$75",
  "green": "$23"
}

print('Choose a color to paint the wall:')
color = str(input())
print('Cost of purchasing', color, 'paint:', thisdict[color])