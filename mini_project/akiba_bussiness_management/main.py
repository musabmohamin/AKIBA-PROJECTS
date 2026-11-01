from product import (
    add_product,
    search_product,
    update_product_info,
    display,
    validator
)

from sales import record_sale
from reports import display_reports

products = [
    {"name": "Laptop", "price": 50000, "quantity": 2},
    {"name": "Mouse", "price": 800, "quantity": 3},
    {"name": "Keyboard", "price": 1500, "quantity": 1},
    {"name": "Headphones", "price": 2000, "quantity": 2},
    {"name": "USB Cable", "price": 300, "quantity": 4},
    {"name": "Monitor", "price": 12000, "quantity": 1}
]
sales ={
    1: {
        "product_name": "Laptop",
        "quantity": 2,
        "unit_price": 50000,
        "total_price": 100000
    },
    2: {
        "product_name": "Mouse",
        "quantity": 5,
        "unit_price": 500,
        "total_price": 2500
    },
    3: {
        "product_name": "Keyboard",
        "quantity": 3,
        "unit_price": 1200,
        "total_price": 3600
    },
    4: {
        "product_name": "Monitor",
        "quantity": 2,
        "unit_price": 12000,
        "total_price": 24000
    },
    5: {
        "product_name": "Headphones",
        "quantity": 4,
        "unit_price": 1500,
        "total_price": 6000
    }
}
while 1:
    print(f"""===== AKIBA BUSINESS TOOLKIT =====

    1. Add Product
    2. View Products
    3. Search Product
    4. Update Product
    5. Record Sale
    6. View Reports
    7. Exit

    Choose an option: 
  

        """)
    while True:
        option = input("Choose an option (1-7): ")

        error = validator(option, "option")

        if error is not None:
            print(error)
            continue

        option = int(option)
        break
    if option == 1:
        print(add_product(products))

    elif option == 2:
        print(display(products))

    elif option == 3:
        print(search_product(products))

    elif option == 4:
        print(update_product_info(products))

    elif option == 5:
        record_sale(products, sales)

    elif option == 6:
        display_reports(products, sales)

    elif option == 7:
        print("Exiting AKIBA BUSINESS TOOLKIT.")
        break


       
        




