class Pizza:
    def __init__(self):
        self.name = ""
        self.size = ""
        self.crust = ""
        self.sauce = ""
        self.meat = ""
        self.cheese = ""
        self.toppings = []
    
    def add_topping(self, topping):
        self.toppings.append(topping)

    def pizza_desc(self):
        print(f'The pizza is {self.size}, has a {self.crust} crust, with {self.sauce} sauce, {self.meat}, {self.cheese}, and has the following extra toppings:')
        for toppings in self.toppings:
            print(toppings)


hawaiian_pizza = Pizza()
hawaiian_pizza.name = "hawiian pizza"
hawaiian_pizza.size = "large"
hawaiian_pizza.crust = "thin"
hawaiian_pizza.sauce = "tomato"
hawaiian_pizza.meat = "bacon"
hawaiian_pizza.cheese = "mozzarella"
hawaiian_pizza.toppings = ["bacon", "pineapple", "jalapenos", "ham"]

hawaiian_pizza.pizza_desc()
hawaiian_pizza.add_topping("olives")