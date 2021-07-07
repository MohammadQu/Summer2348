# Mohammad Qureshi
# PSID 1789301
#LAB 12.9

user_input = input().split()
name = user_input[0]

while name != '-1':
    try:
        age = int(user_input[1]) + 1
    except Exception as string:
        age = 0

    print('{} {}'.format(name, age))
    user_input = input().split()
    name = user_input[0]
