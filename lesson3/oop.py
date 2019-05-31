class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно содержать больше 1 символов')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount
    
    def discounted(self):
        return self.price - self.price * self.discount / 100
    
    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        self.stock -= items_count

    def get_color(self):
        raise NotImplementedError
    
    def __repr__(self):
        return f'Product name: {self.name}, price: {self.price}, stock: {self.stock}'
    


class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color

    def get_color(self):
        return f'Цвет корпуса: {self.color}'
    
    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}'


my_phone = Phone('iPhone', 60000, 'Black')

class Sofa(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture

    def get_color(self):
        return f'Цвет обивки: {self.color}, тип ткани {self.texture}'
    
    def __repr__(self):
        return f'<Sofa name: {self.name}, price: {self.price}, stock: {self.stock}'


my_sofa = Sofa('Veveve', 10000, 'White', 'Leather')

print(my_sofa)

print(my_sofa.color)
print(my_sofa.texture)