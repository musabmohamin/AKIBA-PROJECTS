
def calculate_revenue(sales):
    total_revenue = 0

    for sale in sales.values():
        total_revenue += sale["total_price"]

    return total_revenue


def calculate_inventory_value(products):
    total_value = 0

    for product in products:
        total_value += product["quantity"] * product["price"]

    return total_value


def display_low_stock(products, threshold=5):
    found = False

    for product in products:
        if product["quantity"] < threshold:
            print(
                f"Product: {product['name']} | "
                f"Quantity remaining: {product['quantity']}"
            )
            found = True

    if not found:
        print("No low-stock products.")


def display_sales_summary(sales):
    if not sales:
        print("No sales have been recorded.")
        return

    total_items_sold = 0

    print("\n--- RECORDED SALES ---")

    for sale_id, sale in sales.items():
        print(f"\nSale ID: {sale_id}")
        print(f"Product: {sale['product_name']}")
        print(f"Quantity sold: {sale['quantity']}")
        print(f"Unit price: {sale['unit_price']:.2f} Birr")
        print(f"Total price: {sale['total_price']:.2f} Birr")

        total_items_sold += sale["quantity"]

    print("\n--- SALES TOTALS ---")
    print(f"Number of sales records: {len(sales)}")
    print(f"Total units sold: {total_items_sold}")
    print(f"Total revenue: {calculate_revenue(sales):.2f} Birr")


def display_reports(products, sales):
    print("\n========== BUSINESS REPORT ==========")

    print(
        f"Total revenue: "
        f"{calculate_revenue(sales):.2f} Birr"
    )

    print(
        f"Remaining inventory value: "
        f"{calculate_inventory_value(products):.2f} Birr"
    )

    print("\n--- LOW-STOCK PRODUCTS ---")
    display_low_stock(products)

    display_sales_summary(sales)

    print("\n=====================================")