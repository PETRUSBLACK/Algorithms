asking = input("“What would you like”? (espresso/latte/cappuccino)?        >")

# Creating the Coffee section
class Coffee:
    def __init__(self, water, coffee, milk):


espresso = Coffee(300, 100, 200)
espresso.price = 1.5
espresso.milk = 5
espresso.water = 50
espresso.coffee = 18

latte = Coffee(300, 100, 200)
latte.water = 200
latte.milk = 150
latte.coffee = 24
latte.price = 2.5

cappuccino = Coffee(300, 100, 200)
cappuccino.price = 3.0
cappuccino.water = 250
cappuccino.milk = 100
cappuccino.coffee = 24,
