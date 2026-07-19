

def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Part A - Bug Demonstration")
print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))

print("-" * 40)


def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("Part B - Fixed Function")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", ["bread"]))
print(add_item("eggs"))

print("-" * 40)


def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print("\nTuple cannot be modified.")
        print("Error:", e)


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)
    final_total = total - discount_amount

    return final_total


cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Ravi", 5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

add_to_cart(cart2, "Keyboard", 2000, 1)
add_to_cart(cart2, "Monitor", 15000, 1)

print("Customer 1 Cart")
print(cart1)

print("\nCustomer 2 Cart")
print(cart2)

print("\nCustomer 1 Total:", calculate_total(cart1))
print("Customer 2 Total:", calculate_total(cart2))
price = (1000,2000)
update_price(price, 2000)