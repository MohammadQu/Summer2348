# Mohammad Qureshi
# PSID 1789301
# LAB 11.27


jersey_list = []
rate_list = []

player_dict = {}

print("Enter player 1's jersey number:")
jersey_number = input()
print("Enter player 1's rating:")
player_rating = input()
for num in jersey_number:
    num = int(num)
    jersey_list.append(num)
for num in player_rating:
    num = int(num)
    rate_list.append(num)
player_dict[jersey_number] = player_rating
print()

print("Enter player 2's jersey number:")
jersey_number = input()
print("Enter player 2's rating:")
player_rating = input()
for num in jersey_number:
    num = int(num)
    jersey_list.append(num)
for num in player_rating:
    num = int(num)
    rate_list.append(num)
player_dict[jersey_number] = player_rating
print()

print("Enter player 3's jersey number:")
jersey_number = input()
print("Enter player 3's rating:")
player_rating = input()
for num in jersey_number:
    num = int(num)
    jersey_list.append(num)
for num in player_rating:
    num = int(num)
    rate_list.append(num)
player_dict[jersey_number] = player_rating
print()

print("Enter player 4's jersey number:")
jersey_number = input()
print("Enter player 4's rating:")
player_rating = input()
for num in jersey_number:
    num = int(num)
    jersey_list.append(num)
for num in player_rating:
    num = int(num)
    rate_list.append(num)
player_dict[jersey_number] = player_rating
print()


print("Enter player 5's jersey number:")
jersey_number = input()
print("Enter player 5's rating:")
player_rating = input()
for num in jersey_number:
    num = int(num)
    jersey_list.append(num)
for num in player_rating:
    num = int(num)
    rate_list.append(num)
player_dict[jersey_number] = player_rating
print()


print('ROSTER')

dictionary_items = player_dict.items()
sorted_items = sorted(dictionary_items)
print(sorted_items)
for key, value in sorted_items():
    print('Jersey number: {}, Rating: {}'.format(key, value))


jersey_list.sort()
x = 0
for num in jersey_list:
        print('Jersey number: {}, Rating: {}'.format(num, rate_list[x]))
        #print('Jersey number:', num, 'Rating:', rate_list[x])
        x = x + 1

while True:
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print(' ')
    print('Choose an option:')

    option = str(input())
    counter = 5
    if(option == 'o'):
        print('ROSTER')
        for key, value in player_dict.items():
            print('Jersey number: {}, Rating: {}'.format(key, value))
    elif(option == 'a'):
        newNum = int(input("Enter a new player's jersey number:"))
        newRate = int(input("Enter the player's rating:"))

        jersey_list.append(newNum)
        rate_list.append(newRate)

    elif (option == 'd'):
        del_num = int(input("Enter a jersey number:"))
        for x in range(len(jersey_list)):
            if del_num == jersey_list[x]:
                jersey_list[x].remove
                rate_list[x].remove
        #rate_list.remove(delNum)

    elif (option == 'r'):
        updateRate = int(input("Enter a rating:"))
        print('ABOVE', updateRate)

        for x in range(len(rate_list)):
            if updateRate < rate_list[x]:
                print('Jersey number:', jersey_list[x], 'Rating:', rate_list[x])

    elif (option == 'q'):
        break

