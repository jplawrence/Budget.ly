
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
    elif item == "bread":
        items_in_cart += 1
        print(bread.price)
        cart_total.append(bread.price)
    elif item == "cheese":
        items_in_cart += 1
        print(cheese.price)
        cart_total.append(cheese.price)
    elif item == "butter":
        items_in_cart += 1
        print(butter.price)
        cart_total.append(butter.price)
    elif item == "burgers":
        items_in_cart += 1
        print(burgers.price)
        cart_total.append(burgers.price)
    elif item == "fish_fingers":
        items_in_cart += 1
        print(fish_fingers.price)
        cart_total.append(fish_fingers.price)
    elif item == "apples":
        items_in_cart += 1
        print(apples.price)
        cart_total.append(apples.price)
    elif item == "bananas":
        items_in_cart += 1
        print(bananas.price)
        cart_total.append(bananas.price)
    elif item == "chicken_fillets":
        items_in_cart += 1
        print(chicken_fillets.price)
        cart_total.append(chicken_fillets.price)
    elif item == "lamb":
        items_in_cart += 1
        print(lamb.price)
        cart_total.append(lamb.price)
    elif item == "pork":
        items_in_cart += 1
        print(pork.price)
        cart_total.append(pork.price)
    elif item == "chips":
        items_in_cart += 1
        print(chips.price)
        cart_total.append(chips.price)
    elif item == "oil":
        items_in_cart += 1
        print(oil.price)
        cart_total.append(oil.price)
    elif item == "lettuce":
        items_in_cart += 1
        print(lettuce.price)
        cart_total.append(lettuce.price)
    elif item == "rolls":
        items_in_cart += 1
        print(rolls.price)
        cart_total.append(rolls.price)
    elif item == "ketchup":
        items_in_cart += 1
        print(ketchup.price)
        cart_total.append(ketchup.price)
    elif item == "viennas":
        items_in_cart += 1
        print(viennas.price)
        cart_total.append(viennas.price)
    elif item == "juice":
        items_in_cart += 1
        print(juice.price)
        cart_total.append(juice.price)
    elif item == "water":
        items_in_cart += 1
        print(water.price)
        cart_total.append(water.price)
    elif item == "mince":
        items_in_cart += 1
        print(mince.price)
        cart_total.append(mince.price)
    elif item == "bacon":
        items_in_cart += 1
        print(bacon.price)
        cart_total.append(bacon.price)
    elif item == "nesquik":
        items_in_cart += 1
        print(nesquik.price)
        cart_total.append(nesquik.price)
    elif item == "pasta":
        items_in_cart += 1
        print(pasta.price)
        cart_total.append(pasta.price)
    elif item == "takeouts":
        items_in_cart += 1
        print(takeouts.price)
        cart_total.append(takeouts.price)

print("Items in cart: " + str(items_in_cart))
print("Total: $" + str(round(sum(cart_total))))
