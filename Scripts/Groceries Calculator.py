
class Product:
    def __init__(self, price):
        self.price = price


milk = Product(2.5)
eggs = Product(1.5)
bread = Product(3)
cheese = Product(2.9)
butter = Product(3)
burgers = Product(8)
fish_fingers = Product(5)
apples = Product(5)
bananas = Product(1.5)
chicken_fillets = Product(8.9)
lamb = Product(10)
pork = Product(7)
chips = Product(2)
oil = Product(2)
lettuce = Product(2)
rolls = Product(3.5)
ketchup = Product(3)
viennas = Product(3.5)
juice = Product(2)
water = Product(1)
mince = Product(10)
bacon = Product(4.5)
nesquik = Product(4.5)
pasta = Product(1.5)
takeouts = Product(15)

a = int(input("How many items would you like to add to your cart? "))
items_in_cart = 0
cart_total = []
reached = False
while items_in_cart < a:
    item = input("Add item: ")
    if item == "eggs" and not reached:
        eggs_item = True
        items_in_cart += 1
        print(eggs.price)
        cart_total.append(eggs.price)
    elif item == "milk" and not reached:
        milk_item = True
        items_in_cart += 1
        print(milk.price)
        cart_total.append(milk.price)


print("Items in cart: " + str(items_in_cart))
print("Total: $" + str(round(sum(cart_total))))