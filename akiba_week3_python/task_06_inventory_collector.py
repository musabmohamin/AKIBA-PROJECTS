
inventory = [
    ["Mouse", 10, 500],
    ["Keyboard", 5, 1200],
    ["Monitor", 8, 6500],
    ["USB Cable", 20, 250],
    ["Headphones", 12, 1800],
    ["Laptop", 4, 45000],
    ["Webcam", 6, 2500],
    ["Flash Drive", 15, 400],
    ["Printer", 3, 12000],
    ["Power Bank", 7, 2200]
]
threshold_low_stock = 5


def add_product():
        while True:
                product_name = input("Enter product name: ").strip()

                for product in inventory:
                        if product[0].lower() == product_name.lower():
                         return "Product name already exists. Update the existing product instead."

                if product_name == "":
                     return "Product name cannot be empty."

                price = int(input("Enter product price in Birr: "))
                if price < 0:
                     return "Price cannot be negative."

                stock = int(input("Enter initial stock quantity: "))
                if stock < 0:
                     return "Stock quantity cannot be negative."

                inventory.append([product_name, stock, price])
                add = int(input("Enter 1 to add another product or 0 to finish: "))

                if add != 1:
                        return inventory


def search_product():
        search_name = input("Enter the product name to search for: ").strip().lower()

        if search_name == "":
             return "No product name was entered."

        for product in inventory:
            if product[0].lower() == search_name:
                return product

        return "Product not found."


def update_product_price():
        name_update = input("Enter the name of the product to update: ")
        update_price = int(input("Enter the new price in Birr: "))

        if update_price < 0:
             return "Price cannot be negative."

        for product in inventory:
                if product[0].lower() == name_update.strip().lower():
                    product[2] = update_price
                    return "Product price updated:", product

        return "Product not found."


def increase_stock():
       name_to_increase = input("Enter the product name: ")
       amount_to_increase = int(input("Enter the quantity to add to stock: "))

       if amount_to_increase < 0:
            return "Stock increase cannot be negative."

       for product in inventory:
              if product[0].lower() == name_to_increase.strip().lower():
                  product[1] = product[1] + amount_to_increase
                  return "Stock increased successfully:", product

       return "Product not found."


def sell_product():
       sell = []
       name_to_sell = input("Enter the product name to sell: ")
       amount_to_sell = int(input("Enter the quantity to sell: "))

       if amount_to_sell <= 0:
            return "Quantity must be greater than zero."

       for product in inventory:
                if name_to_sell.strip().lower() == product[0].lower():
                        if product[1] < amount_to_sell:
                                return "Insufficient stock. The requested quantity exceeds available stock."

                        sell.append([product[0], amount_to_sell])
                        product[1] = product[1] - amount_to_sell

                        return sell

       return "Product not found."


def calculate_inventory():
       total = 0

       for product in inventory:
              product_inventory = product[1] * product[2]
              total += product_inventory

       return total


def low_stock_report(threshold_low_stock):
       low_stock = []

       for product in inventory:
              if product[1] < threshold_low_stock:
                     low_stock.append(product)

       return low_stock


while True:
        print("""========== INVENTORY MANAGEMENT SYSTEM ==========

                1. Search for a product
                2. Add a new product
                3. Update product price
                4. Increase stock quantity
                5. Sell a product
                6. Calculate total inventory value
                7. Generate low-stock report
                8. Display all products
                0. Exit

                =================================================
                """)

        choose = int(input("Enter your choice (0–8): "))

        if choose == 1:
                search = search_product()
                print("Search result:", search)

        elif choose == 2:
                add = add_product()
                print("Inventory:", add)

        elif choose == 3:
                update = update_product_price()
                print(update)

        elif choose == 4:
               increase = increase_stock()
               print("Updated inventory:", increase)

        elif choose == 5:
               sell = sell_product()
               print("Sales result:", sell)

        elif choose == 6:
               total = calculate_inventory()
               print(f"Total inventory value: {total:,} Birr")

        elif choose == 7:
               low_stock = low_stock_report(threshold_low_stock)
               print("Low-stock report:", low_stock)

        elif choose == 8:
              print("========== ALL PRODUCTS ==========")

              for product in inventory:
                  print(
                      f"Product: {product[0]}\n"
                      f"Stock quantity: {product[1]}\n"
                      f"Unit price: {product[2]:,} Birr\n"
                  )

        elif choose == 0:
              print("Exiting the Inventory Management System. Goodbye!")
              break

        else:
              print("Invalid choice. Please enter a number from 0 to 8.")