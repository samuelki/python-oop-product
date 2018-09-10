class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.tax = tax
        self.price = self.price*tax + self.price
        return self

    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
        elif reason_for_return == "like_new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            self.price *= 0.8
        return self
    
    def display_info(self):
        print("Price:", self.price)
        print("Item name:", self.item_name)
        print("Weight:", self.weight)
        print("Brand:", self.brand)
        print("Satus:", self.status)
        print("")
        return self

product1 = Product(140, "Airpods", "2 lbs", "Apple")

product1.display_info().add_tax(0.10).display_info().return_item("opened").display_info()


