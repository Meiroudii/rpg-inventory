current_inventory = ["shoes", "sword of ozx", 1, "death", "life", "choco orb"]

def show_inventory():

    item_query = input("Name of item: ")
    is_exist = item_query.lower() in current_inventory
    if is_exist:
        try:
            show_item_inventory = current_inventory.index(str(item_query))
            current_inventory[show_item_inventory]
            print(f"item: {item_query} is in the inventory\nLocation: {show_item_inventory + 1}: {len(current_inventory)}")
        except ValueError:
            print("Item does not exist")
    else:
        print("Something went wrong")

def add_item(item):
    current_inventory.append(item)
    print(current_inventory)
def main():
    while True:
        print(f"\tBag\n[1] Add Item\n[2] Search Item\n\tCtrl+c QUIT")
        try:
            select_options = int(input("\t>> "))
            if select_options == 1:
                while True:
                    insert_new_item = input("Item name: ")
                    add_item(insert_new_item)
                    confirmation_to_quit = input("Added sucessfully\nwould you like to add again? (y/n)")
                    if confirmation_to_quit.lower() == 'y':
                        continue
                    else:
                        break
            elif select_options == 2:
                while True:
                    show_inventory()
                    confirmation_to_quit = input("[y]Search again\n[n]Go to main menu\n ")
                    if confirmation_to_quit.lower() == 'y':
                        continue
                    else:
                        break
        except ValueError:
            print("Type error try again")
            break



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(" [ System shutdown ] ")

