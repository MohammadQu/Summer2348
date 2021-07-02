# Mohammad Qureshi
# PSID 1789301
# FINAL PROJECT PART 1

import csv
from datetime import datetime

# CLASS FOR STORING INVENTORY DETAILS
class Inventory:

    def __init__(self, item_id, manufacture, item_type, price, service_date, damaged=True):
        self.item_id = item_id
        self.manufacture = manufacture
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.damaged = damaged

    # RETURN NAME OF MANUFACTURER
    def get_manufacture(self):
        return self.manufacture

    # RETURN THE ITEM ID
    def get_item_id(self):
        return self.item_id

    # RETURN SERVICE DATE
    def get_service_date(self):
        date_format = datetime.strptime(self.service_date.strip(), "%m/%d/%Y")
        return date_format

    # RETURN PRICE
    def get_price(self):
        return float(self.price)

    # RETURN TRUE IF DAMAGED, OTHERWISE FALSE
    def is_damaged(self):
        return self.damaged

    # RETURN ALL ATTRIBUTES OF CLASS INTO A LIST
    def get_all_attribute_list(self, show_damaged=True):

        # IF DAMAGED, ADD INTO THE LIST, ELSE SKIP
        if self.damaged:
            damaged = "damaged"
        else:
            damaged = ""
        if show_damaged:
            return [self.item_id, self.manufacture, self.item_type, self.price, self.service_date, damaged]
        return [self.item_id, self.manufacture, self.item_type, self.price, self.service_date]

# FUNCTION TO INPUT 3 CSV FILES AND ORGANIZE DATA
def read_inventory_file():
    full_inventory = []
    manufacturer = []
    service_date_list = []
    price_list = []

    file = open("ManufacturerList.csv", "r")  # opening entered file in read mode

    csv_file = csv.reader(file)
    for row in csv_file:
        manufacturer.append(row)

    file.close()  # closing the file

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

    # USING FOR LOOPS, CREATE INSTANCES
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

# FUNCTION FOR WRITING SORTED ITEMS BACK TO THE FILE
# IF SHOW_DAMAGED = TRUE, DAMAGED WILL BE ADDED TO CSV FILE
# SAVE_TO IS THE NAME OF THE FILE TO SAVE
# INVENTORIES IS THE LIST OF OBJECTS IN THE CLASS
# NO RETURN, THE FUNCTION IS CALLED WITHIN OTHER FUNCTIONS
def write_sorted_item_file(save_to, inventories, show_damaged=True):
    # SAVING SORTED ITEMS BACK TO THE CSV
    # OPENING FILE IN WRITE MODE
    file = open(save_to, "w", newline="")

    writer = csv.writer(file)

    # WRITING ROWS TO THE FILE
    for inventory in inventories:
        writer.writerow(inventory.get_all_attribute_list(show_damaged))

    file.close()
    print("Sorted items saved to file: {}\n".format(save_to))

# FUNCTION FOR READING CSV FILES AND SORTING DATA BY MANUFACTURER NAME
# SAVE_TO IS THE NAME OF THE FILE TO SAVE
def read_sort_write_full_inventory(save_to):

    # CALL BACK TO PREVIOUS FUNCTION
    full_inventory = read_inventory_file()

    print("Sorting file items according to manufacturer name...")
    # SORT INVENTORY ACCORDING TO MANUFACTURER NAME USING BUBBLE SORT ALGORITHM
    for i in range(len(full_inventory)):
        for j in range(len(full_inventory) - 1 - i):
            if full_inventory[j].get_manufacture() > full_inventory[j + 1].get_manufacture():
                temp = full_inventory[j]
                full_inventory[j] = full_inventory[j + 1]
                full_inventory[j + 1] = temp

    # CALL BACK TO PREVIOUS FUNCTION
    # WRITE SORTED DATA
    write_sorted_item_file(save_to, full_inventory)


# FUNCTION USED TO SORT THE INVENTORY BY ITEM ID
# CALL BACK TO INVENTORY CLASS FOR inventories
def sort_inventory(inventories):
    for i in range(len(inventories)):
        for j in range(len(inventories) - 1 - i):
            if inventories[j].get_manufacture() > inventories[j + 1].get_manufacture():
                temp = inventories[j]
                inventories[j] = inventories[j + 1]
                inventories[j + 1] = temp


# FUNCTION FOR WRITING INVENTORIES ACCORDING TO ITEM ID FOR EACH ITEM TYPE
def read_sort_write_all_types_inventory():

    # CALL BACK TO PREVIOUS FUNCTION
    inventories = read_inventory_file()

    # CREATE LIST TO ADD ALL ITEM TYPES
    item_types = []

    # FOR LOOP TO ADD ALL ITEM TYPES FROM INVENTORY
    for inventory in inventories:
        item_types.append(inventory.item_type)

    # USE A SET TO REMOVE DUPLICATES, AND HAVE UNIQUE ITEMS
    item_types = list(set(item_types))

    # FOR LOOP TO GO THROUGH EACH ITEM TYPE
    # CREATE A TEMPORARY INVENTORY LIST TO ADD ITEMS OF THE SAME TYPE
    # USE A NESTED FOR LOOP TO GO THROUGH EACH INVENTORY ITEM OF EACH ITEM TYPE.
    for item_type in item_types:
        temp_inventory = []
        for inventory in inventories:
            if item_type == inventory.item_type:
                temp_inventory.append(inventory)

        # CALL BACK TO SORT_INVENTORY FUNCTION AND WRITE_SORTED_ITEM_FILE FUNCTION
        # CREATE NEW CSV FILES WITH THE ITEM TYPE ADDED TO THE NAME
        print("Sorting file items according to item ID...")
        sort_inventory(temp_inventory)
        write_sorted_item_file("{}Inventory.csv".format(item_type.title()), temp_inventory)


# FUNCTION TO READ CSV FILES AND SORT ITEMS BY SERVICE DATE
# SAVE_TO IS THE NAME OF THE FILE TO SAVE
def read_sort_write_past_service_date_inventory(save_to):

    # CALL BACK TO PREVIOUS FUNCTION, READ_INVENTORY_FILE
    past_date_inventory = read_inventory_file()

    print("Sorting file items according to service dates...")
    # SORTING INVENTORY ACCORDING TO SERVICE DATE USING BUBBLE SORT ALGORITHM
    for i in range(len(past_date_inventory)):
        for j in range(len(past_date_inventory) - 1 - i):
            if past_date_inventory[j].get_service_date() > past_date_inventory[j + 1].get_service_date():
                temp = past_date_inventory[j]
                past_date_inventory[j] = past_date_inventory[j + 1]
                past_date_inventory[j + 1] = temp

    write_sorted_item_file(save_to, past_date_inventory)  # writing sorted data


# FUNCTION FOR READING CSV FILE AND SORTING ITEMS BY PRICE
# SAVE_TO IS THE NAME OF THE FILE TO SAVE
def read_sort_write_damaged_inventory(save_to):

    # CALL BACK TO PREVIOUS FUNCTION
    inventories = read_inventory_file()

    # CREATE A DAMAGED_INVENTORY LIST
    damaged_inventory = []

    # USING FOR LOOP, GO THROUGH INVENTORY AND LOCATE DAMAGED ITEMS
    # USING IF STATEMENT, ADD DAMAGED INVENTORY TO DAMAGED_INVENTORY LIST
    for inventory in inventories:
        if inventory.is_damaged():
            damaged_inventory.append(inventory)

    print("Sorting file items according to price...")

    for i in range(len(damaged_inventory)):
        for j in range(len(damaged_inventory) - 1 - i):
            if damaged_inventory[j].get_price() < damaged_inventory[j + 1].get_price():
                temp = damaged_inventory[j]
                damaged_inventory[j] = damaged_inventory[j + 1]
                damaged_inventory[j + 1] = temp

    write_sorted_item_file(save_to, damaged_inventory, show_damaged=False)



read_sort_write_full_inventory("FullInventory.csv")
read_sort_write_all_types_inventory()
read_sort_write_past_service_date_inventory("PastServiceDateInventory.csv")
read_sort_write_damaged_inventory("DamagedInventory.csv")