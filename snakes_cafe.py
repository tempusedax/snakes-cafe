
print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
apps = {
    "Wings": "0",
    "Cookies": "0",
    "Spring Rolls": "0"
}

entre = {
    "Salmon": "0",
    "Steak": "0",
    "Meat Tornado": "0",
    "A Literal Garden": "0"
}

dess = {
    "Ice Cream": "0",
    "Cake": "0",
    "Pie": "0"
}

order = ""
# n = 0
# report = f"** {n + 1} order of {order} have been added to your meal **"
# print(report)
num = 1
food = []
while order != "quit":
    order = input("> ")
    if order not in food:
        food.append(order)
        print(food)
        report = f"** {food.count(order)} order of {order} have been added to your meal **"
        print(report)
    else:
        food.append(order)
        report = f"** {food.count(order)} orders of {order} have been added to your meal **"
        print(report)





