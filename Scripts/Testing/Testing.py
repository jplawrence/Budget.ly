class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Object Transformer


input_products = ["eggs", "milk", "bread", "cheese"]
prices = [1.5, 2.3, 3, 5]
outlist = []
outlist_prices = []
output = {}
g = 0
f = 0


for i in input_products:
    output[i] = Product(input_products[g], prices[g])
    g += 1

# Putting Objects in List

length = len(input_products)

while f < length:
    outlist.append(output[input_products[f]].name)
    outlist_prices.append(output[input_products[f]].price)
    f += 1

# Input Code Begins

new_cart = []
total = []


a = " "

while a != "":
    item = input("Add item: ")
    if item in outlist:
        # number of items in cart
        new_cart.append(item)
        # goes at the end
        count_of_item = new_cart.count(item)
        # total
        index_position = outlist.index(item)
        total.append(outlist_prices[index_position])
    elif item == "":
        break
    else:
        print("No")


print(f"""Order Sheet Summary:
Total Amount of items: {len(new_cart)}
Total Amount: ${sum(total)}
-----------
Amount of items:
""")

cart_set = set(new_cart)

for item in cart_set:
    print(f"{item}: {new_cart.count(item)}")

