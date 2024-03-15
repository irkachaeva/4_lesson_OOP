class Category:
    name: str #название
    description: str #описание
    products: list #товары

    count_of_category = 0
    count_uniq_category = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.count_of_category = 1

        Category.count_uniq_category += 1


class Product:
    name: str #название
    description: str #описание
    price: float #цена
    quantity_stock: int #количество в наличии


    def __init__(self, name, description, price, quantity_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_stock = quantity_stock


