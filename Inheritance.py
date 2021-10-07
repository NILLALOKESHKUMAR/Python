class Product:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def getPrice(self):
        print(self.price)

    def setPrice(self, price):
        self.price = price

    def getProductDetails(self):
        print(self.brand, self.model)
        print("RS.", self.price)


class Electronics(Product):
    def __init__(self, brand, model, price, processor, ram, storage):
        super().__init__(brand, model, price)
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def getProductDetails(self):
        print(self.brand, self.model)
        print("RS.", self.price)
        print(self.ram, "gb ram")
        print(self.storage, "gb Internal Storage")


class Laptop(Electronics):
    def __init__(self, brand, model, price, processor, ram, storage, ports):
        print("product added to the inventory")
        super().__init__(brand, model, price, processor, ram, storage)
        self.ports = ports

    def getProductDetails(self):
        print(self.brand, self.model)
        print("RS.", self.price)
        print(self.ram, "gb ram")
        print(self.storage)
        print(self.ports)
