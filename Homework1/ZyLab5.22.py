# Mohammad Qureshi
# PSID 1789301
# LAB 5.22


# PART 1
# OUTPUT MENU
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()


# CREATE DICTIONARY
thisdict = {
  "Oil change": "$35",
  "Tire rotation": "$19",
  "Car wash": "$7",
  "Car wax": "$12",
  "-": "No service"
}

# PART 2
# INPUT 2 SERVICES
print('Select first service:')
first = input()
print('Select second service:')
second = input()
print()


# OUTPUT INVOICE
print("Davy's auto shop invoice")
print()
service_one = first
service_two = second
if(service_one == '-'):
  print('Service 1: No service')
else:
  print('Service 1:', service_one, ',', thisdict[service_one])
if(service_two == '-'):
  print('Service 2: No service')
else:
  print('Service 2:', service_two, ',', thisdict[service_two])
