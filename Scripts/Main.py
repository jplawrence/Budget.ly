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

    print(f""""
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
