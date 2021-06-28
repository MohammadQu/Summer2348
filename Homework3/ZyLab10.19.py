# Mohammad Qureshi
# PSID 1789301
# LAB 10.19



class ItemToPurchase:

    def __init__(self):
        self.name = "none"
        self.price = 0
        self.quantity = 0
        self.description = "none"

    def item_name(self, name):
        self.name = name

    def item_price(self, price):
        self.price = price

    def item_quantity(self, quantity):
        self.quantity = quantity

    def item_description(self, description):
        self.description = description

    def print_cost(self):
        print("{} {} @ ${} = ${}".format(self.name, self.quantity, self.price, self.quantity * self.price))

    def print_description(self):
        print("{}: {}".format(self.name, self.description))
        #print(self.name + ": " + self.description)

class ShoppingCart:

    def __init__(self, name="none", date="January 1, 2016"):
        self.cart_list = []
        self.customer_name = name
        self.current_date = date

    def add_item(self, cartItem):
        self.cart_list.append(cart_item)

    def remove_item(self, item_name):
        counter = 0
        cart = self.cart_list[:]
        for m in range(len(cart)):
            item = cart[m]
            if item.name == item_name:
                del self.cart_list[m]
                counter = counter + 1

        if counter == 0:
            print(" ")
            print("Item not found in cart. Nothing removed.")

    def modify_item(self):
        print('CHANGE ITEM QUANTITY')
        print()
        name = str(input('Enter the item name: '))

        for item in self.cart_list:
            # If item found update Quantity in the list
            if (item.item_name == name):
                quantity = int(input('Enter the new quantity: '))
                item.item_quantity = quantity
                flag = True
                break
            else:
                flag = False

        if (flag == False):
            print('Item not found in cart. Nothing modified')


    def get_num_items_in_cart(self, item):
        counter = 0
        cart = self.cart_list[:]
        for i in range(len(cart)):
            item = cart[i]
            counter = counter + cart.quantity
        return counter

    def get_cost_of_cart(self):
        cost = 0
        cart = self.cart_list[:]
        for i in range(len(cart)):
            item = cart[i]
            cost = cost + (item.quantity * item.price)

        return cost

    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        counter = len(self.cart_list)
        if counter == 0:
            print(" ")
            print("SHOPPING CART IS EMPTY")
            return 0
        print("Number of Items: {}".format(counter))
        print(" ")

        for item in self.cart_list:
            item.print_cost()

        total = self.get_cost_of_cart()
        print("Total: ${}".format(total))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print()

        print("Item Descriptions")
        for item in self.cart_list:
            item.print_description()

def print_menu(cart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")



if __name__ =="__main__":

    print("Enter customer's name:")
    customer = input()
    print("Enter today's date:")
    date = input()
    print()

    print("Customer name:", customer)
    print("Today's date:",  date)
    print()
    shopping_cart = ShoppingCart(customer, date)

    option = ""
    print_menu(shopping_cart)
    print()
    while option != "q":
        print('Choose an option:')
        option = input()

        if option == "a":
            print("ADD ITEM TO CART")
            print('Enter the item name: ')
            new_item = input()
            print('Enter the item description')
            new_description = input()
            print('Enter the item price')
            new_price = int(input())
            print('Enter the item quantity')
            new_quantity = int(input())
            print(" ")
            cart_item = ItemToPurchase()
            cart_item.item_name(new_item)
            cart_item.item_description(new_description)
            cart_item.item_price(new_price)
            cart_item.item_quantity(new_quantity)
            shopping_cart.add_item(cart_item)

        elif option == "o":
            shopping_cart.print_total()
            print_menu(shopping_cart)
            continue

        elif option == "r":
            print("REMOVE ITEM FROM CART")
            print('Enter name of item to remove')
            remove_item = input()
            shopping_cart.remove_item(remove_item)

        elif option == "c":
            shopping_cart.modify_item()

        elif option == 'i':
            shopping_cart.print_descriptions()