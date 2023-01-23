class Product:
    # 构造函数
    def __init__(self, order_number, name, price, total_quantity, remaining_quantity):
        self.__id = order_number
        self.__name = name
        self.__price = price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = remaining_quantity

    # 显示商品信息的函数
    def display(self):
        print("ID:", self.__id)
        print("Name:", self.__name)
        print("Price:", self.__price)
        print("Total Quantity:", self.__total_quantity)
        print("Remaining Quantity:", self.__remaining_quantity)

    # 商品价值函数
    def income(self):
        sold_quantity = self.__total_quantity - self.__remaining_quantity
        return sold_quantity * self.__price

    # 修改商品属性函数
    def setdata(self, name=None, price=None, total_quantity=None, remaining_quantity=None):
        if name:
            self.__name = name
        if price:
            self.__price = price
        if total_quantity:
            self.__total_quantity = total_quantity
        if remaining_quantity:
            self.__remaining_quantity = remaining_quantity


# 加入数据
p1 = Product(1, "Watermelon", 15, 800, 600)
p2 = Product(2, "Strawberry", 30, 400, 300)
p3 = Product(3, "litchi", 25, 500, 400)


