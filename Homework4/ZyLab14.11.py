# Mohammad Qureshi
# PSID 1789301
# LAB 14.11


def selection_sort_descend_trace(user_list):
    for x in range(len(user_list) - 1):
        next = x
        for y in range(x + 1, len(user_list)):
            if user_list[y] > user_list[next]:
                next = y
        temp = user_list[x]
        user_list[x] = user_list[next]
        user_list[next] = temp
        print(' '.join([str(z) for z in user_list]), end=' ')
        print()
    return user_list

if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(input_numbers)
