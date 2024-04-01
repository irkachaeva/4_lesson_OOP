class Product:
    name: str #название
    description: str #описание
    price: float #цена
    quantity_stock: int #количество в наличии

    def __init__(self, name, description, price, quantity_stock):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_stock = quantity_stock

    @property
    def price(self):
        '''геттер для атрибута цены.'''
        return self.__price

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity_stock: int):
        '''создание нового товара'''
        return cls(name, description, price, quantity_stock)

    @price.setter
    def price(self, new_price):
        '''cеттер для атрибута цены. В случае если цена равна или ниже нуля,
             выводится сообщение в консоль, при этом новая цена не устанавливается.'''
        if new_price <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = new_price #устанавливаем цену, если она удовлетворяет условию выше

    def __str__(self):
        ''' строковое отображение в виде:Название продукта, 80 руб. Остаток: 15 шт.'''
        return f'{self.name} {self.price}руб. Остаток: {self.quantity_stock} шт.'

    def __add__(self, other):
        '''складываем объекты между собой таким образом,
        чтобы результат выполнения сложения двух продуктов был сложением сумм,
        умноженных на количество на складе.'''
        if type(self) == type(other):
            return self.quantity_stock * self.price + other.quantity_stock * other.price
        raise TypeError('Можно складывать товары только из одинаковых классов продуктов')


class Smartphone(Product):

    def __init__(self, name, description, price, quantity_stock, productivity, model, memory, color):
        super().__init__(name, description, price, quantity_stock)
        self.productivity = productivity #производительность
        self.model = model #модель
        self.memory = memory #объем встроенной памяти
        self.color = color #цвет.


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity_stock, country, germination_period, color):
        super().__init__(name, description, price, quantity_stock)
        self.country = country #страна - производитель
        self.germination_period = germination_period #срок прорастания,
        self.color = color #цвет.

