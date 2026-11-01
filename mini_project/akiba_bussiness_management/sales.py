def validator(value,rule):
    
    if rule=="name":
        value=value.strip()
        if value=="":
            return "please enter product name"
        return None 
    
    elif rule=="quantity":
        if value=="":
            return"Quantity cannot be empty. Please enter a quantity."
        
        try:
            number = int(value)
        except ValueError:
            return "Invalid quantity. Please enter a whole number."
        if number<0:
            return "Quantity cannot be negative."
        return None
    elif rule == "price":
        if value == "":
            return "Please enter a price."

        try:
            number = float(value)
        except ValueError:
            return "Please enter a valid number."

        if number < 0:
            return "Price cannot be negative."
  
    elif rule == "option":
        
        if value not in ("1", "2", "3", "4", "5", "6", "7"):
            return "Invalid option. Please enter a number from 1 to 7."

        return None
    elif rule=="option add":
        if value not in("1","0"):
            return "invalid option"



def record_sale(products, sales):

    while True:
        sale = input("Enter product name to sell: ").strip()

        error = validator(sale, "name")
        if error is not None:
            print(error)
            continue

        product_found = None

        for product in products:
            if product["name"].lower() == sale.lower():
                product_found = product
                break

        if product_found is None:
            print("There is no product with this name.")
            continue

        quantity_sale = input("Enter quantity to sell: ")

        error = validator(quantity_sale, "quantity")0
        if error is not None:
            print(error)
            continue

        quantity_sale = int(quantity_sale)

        if product_found["quantity"] < quantity_sale:
            print("Insufficient stock. The requested quantity exceeds available inventory.")
            continue

        unit_price = product_found["price"]
        total_price = calculate_sales(unit_price, quantity_sale)

        sale_id = max(sales.keys(), default=0) + 1

        sales[sale_id] = {
            "product_name": sale,
            "quantity": quantity_sale,
            "unit_price": unit_price,
            "total_price": total_price
        }

        product_found["quantity"] -= quantity_sale

        print("Sale recorded successfully.")
        print("Total price:", total_price)

        sale_more = input("Enter 1 to add another sale or 0 to finish: ")

        error = validator(sale_more, "option add")
        if error is not None:
            print(error)
            continue

        if sale_more == "0":
            break

    return sales


def calculate_sales(price, quantity):
    return price * quantity