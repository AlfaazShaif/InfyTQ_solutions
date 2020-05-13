flowers = {"Orchid": 15, "Rose": 25, "Jasmine": 40}


class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None

    def get_flower_name(self):
        return self.__flower_name

    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name

    def get_price_per_kg(self):
        return self.__price_per_kg

    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg

    def get_stock_available(self):
        return self.__stock_available

    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available

    def validate_flower(self):
        for flower, level in flowers.items():
            if self.__flower_name.upper() == flower.upper():
                return True
            else:
                return False

    def validate_stock(self, required_quantity):
        if self.__stock_available > required_quantity:
            return True
        else:
            return False

    def sell_flower(self, required_quantity): 
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= required_quantity

    def check_level(self):
        if self.__stock_available < flowers[self.__flower_name]:
            return True
        else:
            return False


flower1 = Flower()
flower1.set_flower_name("Rose")
flower1.set_price_per_kg(50)
flower1.set_stock_available(20)
print(flower1.sell_flower(15))
print(flower1.check_level())