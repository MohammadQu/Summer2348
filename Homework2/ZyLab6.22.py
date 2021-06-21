# Mohammad Qureshi
# PSID 1789301
# LAB 6.22

# INPUT FIRST EQUATION
first_x = int(input())
first_y = int(input())
first_answer = int(input())

# INPUT SECOND EQUATION
second_x = int(input())
second_y = int(input())
second_answer = int(input())

solution = False

for x in range(-10, 10):
    for y in range(-10,10):
        if (first_x * x) + (first_y * y) == first_answer:
            if (second_x * x) + (second_y * y) == second_answer:
                print(x, y)
                solution = True
    if solution == True:
        break

else:
    print('No solution')
