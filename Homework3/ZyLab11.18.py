# Mohammad Qureshi
# PSID 1789301
# LAB 11.18


user_input = input().split()

integer_list = []

for i in user_input:
    i = int(i)
    if i >= 0:
        integer_list.append(i)

integer_list.sort()
for i in integer_list:
    print(i, end=' ')