# Mohammad Qureshi
# PSID 1789301
# LAB 6.17


# INPUT USER PASSWORD AND INITIALIZE A NEW PASSWORD
password = input()
new_password = ''

# INITIALIZE 'i' TO SPECIFY A LOCATION IN THE PASSWORD
i = 0

# CREATE A WHILE LOOP TO GO THROUGH EACH LETTER
# FINISH AT THE END OF THE PASSWORD
while(i < len(password)):
    letter = password[i]
    if (letter == "i"):
        new_password += '!'
    elif (letter == 'a'):
        new_password += '@'
    elif (letter == 'm'):
        new_password +='M'
    elif (letter == 'B'):
        new_password += '8'
    elif (letter == 'o'):
        new_password += '.'
    else:
        new_password += letter

# MOVE TO THE NEXT LETTER IN THE PASSWORD
    i += 1

# WHILE LOOP COMPLETED
# ADD 'q*s' AT THE END OF EVERY PASSWORD
new_password += "q*s"

# OUTPUT THE NEW PASSWORD
print(new_password)

