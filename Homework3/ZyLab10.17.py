# Mohammad Qureshi
# PSID 1789301
# LAB 10.17


class ItemToPurchase:

    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity


    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@ ${}'.format(self.item_price), '= ${}'.format(self.item_price * self.item_quantity))


if __name__ =="__main__":

    item_one = ItemToPurchase()
    print('Item 1')

    print('Enter the item name:')
    name1 = str(input())
    print('Enter the item price:')
    price1 = int(input())
    print('Enter the item quantity:')
    quantity1 = int(input())


    item_one.item_name = name1
    item_one.item_price = price1
    item_one.item_quantity = quantity1
    print()


    item_two = ItemToPurchase()
    print('Item 2')

    print('Enter the item name:')
    name2 = str(input())
    print('Enter the item price:')
    price2 = int(input())
    print('Enter the item quantity:')
    quantity2 = int(input())

#item_two = ItemToPurchase(name2, price2, quantity2)
    item_two.item_name = name2
    item_two.item_price = price2
    item_two.item_quantity = quantity2
    print()



    print('TOTAL COST')
    item_one.print_item_cost()
    item_two.print_item_cost()
    print()

    Total = ((item_one.item_price * item_one.item_quantity) + (item_two.item_price * item_two.item_quantity))
    print('Total: ${}'.format(Total))