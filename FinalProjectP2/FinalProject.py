# Mohammad Qureshi
# PSID 1789301
# FINAL PROJECT


import csv
from datetime import datetime


class Inventory:
    # CLASS FOR STORING INVENTORY DETAILS
    def __init__(self, item_id, manufacture, item_type, price, service_date, damaged=True):
        self.item_id = item_id
        self.manufacture = manufacture
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.damaged = damaged

    def get_manufacture(self):
        # METHOD TO RETURN MANUFACTURER NAME
        return self.manufacture

    def get_item_id(self):
        # METHOD TO RETURN ITEM ID
        return self.item_id

    def get_service_date(self):
        # METHOD TO RETURN SERVICE DATE
        date_format = datetime.strptime(self.service_date.strip(), "%m/%d/%Y")
        return date_format

    def get_price(self):
        # METHOD TO RETURN PRICE
        return float(self.price)

    def is_damaged(self):
        # METHOD TO RETURN TRUE OR FALSE IF ITEM IS DAMAGED
        return self.damaged

    def get_all_attribute_list(self, show_damaged=True):
        # METHOD TO RETURN ALL ATTRIBUTES OF THE CLASS INTO A LIST
        # IF SHOW_DAMAGED RETURNS TRUE, ADD TO THE LIST
        if self.damaged:
            damaged = "damaged"
        else:
            damaged = ""
        if show_damaged:
            return [self.item_id, self.manufacture, self.item_type, self.price, self.service_date, damaged]
        return [self.item_id, self.manufacture, self.item_type, self.price, self.service_date]


def check_query(inventories, query):
    # FUNCTION FOR FINDING THE APPROPRIATE ITEM ACCORDING TO THE QUERY
    # INVENTORIES, LIST OF OBJECTS OF INVENTORY CLASS
    # QUERY, QUERY ENTERED BY USER
    query = query.lower().split()
    required_inventory = []
    queried_items = []

    for inventory in inventories:
        # FILTERING DAMAGED PRODUCTS AND PRODUCTS THAT HAVE PASSED THE SERVICE DATE
        if not inventory.is_damaged() and datetime.now() <= inventory.get_service_date():
            required_inventory.append(inventory)

    # FILTERING ITEMS ACCORDING TO THE QUERY
    for inventory in required_inventory:
        if any([str(attr).lower() in query for attr in inventory.get_all_attribute_list()]):
            queried_items.append(inventory)

    return queried_items


def print_considered_items(inventories, item_type):
    # FUNCTION FOR PRINTING ITEMS RELATED TO OTHER MANUFACTURERS
    # INVENTORIES, LIST OF OBJECTS OF INENTORY CLASS
    # ITEM_TYPE, TYPE OF ITEM FROM MANUFACTURE TO DISPLAY
    considered_items = []
    if len(inventories) > 0 and item_type is not None:
        print("You may also consider: ")
        # CHECK FOR OTHER MANUFACTURERS WITH SAME ITEM TYPE
        for item in inventories:
            if item.item_type.lower() == item_type.lower():
                considered_items.append(item)

        # PRINTING FETCHED ITEMS
        for item in considered_items:
            print(", ".join([str(i) for i in item.get_all_attribute_list()]))


def print_items(queried_items):
    # FUNCTION FOR PRINTING ITEMS INPUT ON THE BASIS OF THE QUERY
    # QUERIED ITEM IS THE INPUT ITEM FOR THE QUERY
    # RETURN ITEM_TYPE
    if len(queried_items) < 1:  # if no item retrieved
        print("No such item in inventory")

    elif len(queried_items) == 1:
        print("Your item is: ")
        print(", ".join([str(item) for item in queried_items[0].get_all_attribute_list(show_damaged=False)]))

        return queried_items[0].item_type

    else:
        # IF MORE THAN ONE ITEM IS CALLED FOR, THEN WE OUTPUT THE MOST EXPENSIVE PRODUCT
        required_item = queried_items[0]
        maxi = 0

        for item in queried_items:
            if item.get_price() > maxi:
                required_item = item
                maxi = item.get_price()
                print(required_item.get_all_attribute_list())

        print("Your item is: ")
        print(", ".join([str(item) for item in required_item.get_all_attribute_list(show_damaged=False)]))

        return required_item.item_type


def read_inventory_file():
    # FUNCTION FOR READING THE CSV FILE
    # RETURN LIST OF OBJECTS OF INVENTORY CLASS
    full_inventory = []
    manufacturer = []
    service_date_list = []
    price_list = []

    # OPEN AND READ MANUFACTURER FILE
    file = open("ManufacturerList.csv", "r")

    csv_file = csv.reader(file)
    for row in csv_file:
        manufacturer.append(row)

    # CLOSE FILE
    file.close()

    file = open("ServiceDatesList.csv", "r")

    csv_file = csv.reader(file)
    for row in csv_file:
        service_date_list.append(row)

    file.close()

    file = open("PriceList.csv", "r")

    csv_file = csv.reader(file)
    for row in csv_file:
        price_list.append(row)

    file.close()

    # CREATING INSTANCES
    for manufacture in manufacturer:
        item_id = manufacture[0]
        name = manufacture[1]
        item_type = manufacture[2]
        damaged = manufacture[3]

        if damaged == "":
            damaged = False
        else:
            damaged = True

        for service in service_date_list:
            if service[0] == item_id:
                date = service[1]

                for price in price_list:
                    if price[0] == item_id:
                        item_price = float(price[1])

                        full_inventory.append(Inventory(item_id, name, item_type, item_price, date, damaged))
                        break
                break

    return full_inventory


# MAIN FUNCTION
inventories = read_inventory_file()

while True:
    query = input("\nEnter an item (or 'q' to quit): ")

    if query.lower() == "q":
        print("Thank you!")
        break
    queried_items = check_query(inventories, query)
    print()
    item_type = print_items(queried_items)
    print()
    print_considered_items(inventories, item_type)

