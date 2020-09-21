
monthly_income = 0

print("""
Hi! Welcome to Budget.ly, your personal budgeting app. 
This app will have two different functions, creating a budget, 
and our system building one to suit your needs!
""")

# expenses
rent = 0
car_lease = 0
fuel = 0
food = 0
credit_expense = 0
savings = 0
extras = 0

# price adding list for totals

list_a = []
list_b = []

response = input("Please select an option: (a) Create a budget; (b) System budget build: ").lower()
if response == "a":
    print("Please select how you much you want to pay for the following: ")
    rent = int(input("Rent: "))
    car_lease = int(input("Car: "))
    fuel = int(input("Fuel: "))
    food = int(input("Food: "))
    credit_expense = int(input("Credit expense: "))
    savings = int(input("Average Savings p/m: "))

    list_a.append(rent)
    list_a.append(car_lease)
    list_a.append(fuel)
    list_a.append(food)
    list_a.append(credit_expense)
    list_a.append(savings)

    estimated_income = sum(list_a)
    print(f"You should be earning around ${estimated_income} per month.")

elif response == "b":
    print("Fill out the required information, and answer accordingly")
    monthly_income = int(input("Enter your average monthly income: "))
    fuel_distance = int(input("Average distance travelled every week: "))
    person_coverage = int(input("How many people does this budget cover? "))
    if person_coverage == 1:
        food = 250
    elif person_coverage == 2:
        food = 500
    elif person_coverage == 3:
        food = 750
    elif person_coverage > 3:
        food = 1000
    credit = input("Will you be making any credit purchases/agreements (y) Yes, (n) No: ").lower()
    if credit == "y":
        credit_expense = monthly_income * (10 / 100)
    else:
        credit_expense = 0

    savings = monthly_income * (15 / 100)
    rent = monthly_income * (40 / 100)
    car_lease = monthly_income * (25 / 100)
    fuel = fuel_distance * 0.1

    list_b.append(rent)
    list_b.append(car_lease)
    list_b.append(fuel)
    list_b.append(food)
    list_b.append(credit_expense)
    list_b.append(savings)

    total = sum(list_b)
    leftovers = monthly_income - total

    print(f"""
This is what we suggest: 
Rent: ${rent}
Car lease: ${car_lease}
Fuel: ${fuel}
Food: ${food}
Credit Expense: ${credit_expense}
Savings: ${savings}
----
Total: ${total}
Leftovers: ${leftovers}
""")

else:
    print("You didn't select an option!")

response_food = input("Would you like to use our shopping app? (y) Yes, (n) No: ")
if response_food == "y":
    print("Please select items for weekly shopping. Your grocery allowance will be updated")
    dictionary = {
        "eggs": 1.5,
        "milk": 2.5,
        "bread": 3,
        "cheese": 2.9,
        "butter": 3,
        "burgers": 8,
        "fish fingers": 5,
        "apples": 5,
        "bananas": 1.5,
        "chicken Fillets": 8.9,
        "lamb": 10,
        "pork": 7,
        "chips": 2,
        "oil": 2,
        "lettuce": 2,
        "rolls": 3.5,
        "ketchup": 3,
        "viennas": 3.5,
        "juice": 2,
        "water": 1,
        "mince": 10,
        "bacon": 4.5,
        "pasta": 4.5,
        "nesquik": 1.5,
        "takeouts": 15,
    }

    total_prices = []

    a = " "
    while a != "":
        item = input("Add Item: ")

        if item in dictionary.keys():
            item_price = dictionary.get(item)
            total_prices.append(item_price)
        else:
            print("Sorry, we don't have that item")

        if item == "":
            break

    print(f"""Order Summary:
Total Items: {len(total_prices)}
Total: ${sum(total_prices)}
    """)

    total_end_amount = sum(total_prices)
    food = total_end_amount * 4

    list_c = []

    list_c.append(food)
    list_c.append(rent)
    list_c.append(car_lease)
    list_c.append(fuel)
    list_c.append(credit_expense)
    list_c.append(savings)

    print(f"""
Updated Budget: 
----
Rent: ${rent}
Car lease: ${car_lease}
Fuel: ${fuel}
Food: ${food}
Credit Expense: ${credit_expense}
Savings: ${savings}
----
Total: ${sum(list_c)}
Leftovers: ${monthly_income - sum(list_c)}
    """)

else:
    print("Thank you for using our app!")

