
items = []

def calculate_subtotal(items):
    subtotal = 0

    for item in range(len(items)):
        price_of_items = items[item][3] * items[item][5]
        subtotal += price_of_items

    return subtotal

def calculate_discount(subtotal):
    if subtotal < 1000:
        discount = 0
    elif subtotal <= 2999:
        discount = 0.05 * subtotal
    else:
        discount = 0.10 * subtotal

    return discount

def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate
    return tax

def calculate_total(subtotal, discount, tax):
    total = subtotal - discount + tax
    return total

add_items = int(input("Enter 1 to add product or 0 to continue: "))

while add_items == 1:
    product_name = input("Enter the product name: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter quantity of the product: "))

    items.append([
        "product name", product_name,
        "price", price,
        "quantity", quantity
    ])

    add_items = int(input("Enter 1 to add product or 0 to continue: "))

if len(items) > 0:
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)

    tax_rate = 0.15
    tax = calculate_tax(subtotal - discount, tax_rate)

    total = calculate_total(subtotal, discount, tax)

    print("\n========== SHOPPING RECEIPT ==========")

    for item in items:
        print(
            f"{item[1]} | Price: {item[3]:.2f} Birr "
            f"| Quantity: {item[5]} "
            f"| Total: {item[3] * item[5]:.2f} Birr"
        )

    print("--------------------------------------")
    print(f"Subtotal:          {subtotal:.2f} Birr")
    print(f"Discount:          {discount:.2f} Birr")
    print(f"Tax (15%):         {tax:.2f} Birr")
    print(f"Total with tax:    {total:.2f} Birr")
    print("======================================")

else:
    print("No products were added.")
