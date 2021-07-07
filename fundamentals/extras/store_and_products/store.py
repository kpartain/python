from product import Product

class Store:
    all_stores = []
    def __init__(self, store_name):
        self.store_name = store_name
        self.store_inventory = []
        Store.all_stores.append(self)
# #add_product(self, new_product) -
#  takes a product and adds it to the store
    def add_product(self, product_id):
        productToAdd = Product.all_products[product_id]
        self.store_inventory.append(productToAdd)
        return self
# sell_product(self, store_inventory_id) - 
# remove the product from the store's list of products given the id 
# (assume id is the index of the product in the list) and print its info.
    def remove_product(self, store_inventory_id):
        removedItem = self.store_inventory.pop(store_inventory_id)
        print("Removed:",removedItem.name,"which cost: $",removedItem.price,"and was in category:",removedItem.category)
        return self
# change price - condensed to one method, since we can accept negative
# user will say .02 to increase all 2% and -.5 to decrease all 50%
    def set_Inventory_Price_Increase_or_Decrease(self, percent_change):
        currentInventory = self.store_inventory
        for eachItem in currentInventory:
            eachItem.update_price_percent(percent_change)
        return self


banana = Product("banana", 2.00, "produce")
cereal = Product("Blueberry Morning", 5.50, "pantry")
soap = Product("Dial", 1.00, "household")
soap.print_info()

myStore = Store("Publix")
myStore.add_product(0)
myStore.add_product(1)
myStore.add_product(2)
myStore.set_Inventory_Price_Increase_or_Decrease(-.5)
soap.print_info()