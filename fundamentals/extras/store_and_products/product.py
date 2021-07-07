#a name, a price, and a category, unique_id
#have an array of all products. when one is created, array.length+1 = id
class Product:
    all_products = []
    def __init__(self, product_name, product_price, product_category):
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category
        #this assumes we will not remove products from the array of all product objects
        #but rather only remove products from the store inventory
        #metaphor: yogurt does not get erased from earth when local Safeway runs out of it
        self.product_id = len(Product.all_products) - 1
        Product.all_products.append(self)
# update_price(self, percent_change) - 
# updates the product's price. % can be positive or negative used to avoid true false
    def update_price_percent(self, percent_change):
        self.product_price += (self.product_price * percent_change)
        return self
        #made another function to update just the entire price
    def update_price_new_price(self, new_price):
        self.product_price = new_price
        return self
# print_info(self) - 
# print the name of the product, its category, and its price.
    def print_info(self):
        print("ID:",self.product_id,", Name:",self.product_name,", category:",self.product_category,", price: $",self.product_price)

