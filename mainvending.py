from inventory import Inventory

def main():
    inventory= Inventory()
    less_cash= inventory.get_min_cash()
    print(less_cash.id)
    #compare cash
    print(inventory.greater_cash(0,1))
    #union of items
    print(len(inventory.union_items(0,1)))
    #intersection of items
    print((inventory.intersection_items(0,1))[0].name)
    #difference of items
    print((inventory.difference_items(1, 0))[0].name)

if __name__ == "__main__":
    main()
