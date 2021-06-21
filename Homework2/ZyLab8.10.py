# Mohammad Qureshi
# PSID 1789301
# LAB 8.10


# INPUT A STRING
# REMOVE ALL SPACES
user_input = input()
test = user_input.replace(' ', '')

fail = False

start = 0
length = len(test)
end = length - 1

# CREATE WHILE LOOP THAT COMPARES START AND END
while start < end:
    if test[start] != test[end]:
        fail =  True
        break
    else:
        start += 1
        end -= 1
if(fail):
    print(user_input, 'is not a palindrome')
else:
    print(user_input, 'is a palindrome')