# Theory Answers

## Question 1: Function Design

### 1. Why can a single 100-line function be difficult to maintain?

A function that manages products, processes sales, and generates reports performs too many different tasks. This makes the code difficult to understand, test, debug, and update.

For example, if there is a problem with recording a sale, I may need to search through many lines of code to find the cause. Changing one part may also affect other parts of the program.

### 2. Single-purpose functions

A single-purpose function performs one specific task. This makes the program easier to understand and maintain.

For example:

```python
def calculate_total(price, quantity):
    return price * quantity
```

This function only calculates the total price of a sale.

Other functions can have different responsibilities, such as adding a product, recording a sale, or calculating revenue.

### 3. Parameters and return values

Parameters allow a function to receive the data it needs. Return values allow it to send a result back to the part of the program that called it.

For example:

```python
def calculate_revenue(sales):
    total = 0

    for sale in sales:
        total += sale

    return total


sales = [100, 200, 300]
revenue = calculate_revenue(sales)

print(revenue)
```

Output:

```text
600
```

The `sales` parameter receives the sales data, and `return total` sends the calculated revenue back to the caller.

### 4. Code reuse

Small functions can be called whenever their tasks are needed. This avoids writing the same code multiple times.

For example, I can call `calculate_total(price, quantity)` whenever I need to calculate the total price of a sale.

If I need to change the calculation later, I can update the function in one place.

### 5. Testing and debugging

Small functions are easier to test because each function has a clear responsibility.

For example, I can test `calculate_total()` separately without running the entire business management program. If the result is incorrect, I can focus on that function instead of searching through a large block of code.

### 6. How I would divide the program

I would divide the business management program into smaller functions based on their responsibilities:

- `add_product()` — adds a new product.
- `search_product()` — searches for a product.
- `update_product_info()` — updates product information.
- `record_sale()` — records a sale and updates stock.
- `calculate_revenue()` — calculates total revenue.
- `calculate_inventory_value()` — calculates the value of remaining inventory.
- `display_reports()` — displays the business reports.

I would also organize related functions into separate modules, such as `product.py`, `sales.py`, and `report.py`.

### 7. Poorly organized function and improvement

A poorly organized function may combine several unrelated tasks:

```python
def manage_business():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity
    revenue = total

    print("Product:", name)
    print("Total:", total)
    print("Revenue:", revenue)
```

This function collects product information, calculates a sale total, and handles reporting together.

I would improve it by separating the calculations and responsibilities:

```python
def calculate_total(price, quantity):
    return price * quantity


def display_product(name, price, quantity):
    print("Product:", name)
    print("Price:", price)
    print("Quantity:", quantity)


price = 100
quantity = 3

total = calculate_total(price, quantity)

display_product("Pen", price, quantity)
print("Total:", total)
```

Now each function has a clear purpose, and the calculation can be reused and tested separately.

**Conclusion:** Dividing a large function into smaller, single-purpose functions makes the program easier to read, maintain, reuse, test, and debug.

---

## Question 2: Mutable Data and Function Side Effects

Consider the following code:

```python
def add_item(items, item):
    items.append(item)
    return items


products = ["Pen", "Book"]

result = add_item(products, "Bag")

print(products)
print(result)
```

### 1. Why do both printed results contain the added item?

Both printed results contain `"Bag"` because `products` and the function parameter `items` refer to the same list object.

When the function executes:

```python
items.append(item)
```

it modifies the existing list by adding `"Bag"` to it.

The function then returns that same list. Therefore, both `products` and `result` refer to the list containing all three items.

Output:

```text
['Pen', 'Book', 'Bag']
['Pen', 'Book', 'Bag']
```

### 2. How do lists behave when passed to functions?

Lists are mutable objects, meaning their contents can be changed after they are created.

When I pass a list to a function, the parameter refers to the same list object. If the function modifies the list using methods such as `.append()`, `.remove()`, or `.clear()`, the change can be seen outside the function.

For example:

```python
def add_product(products, product):
    products.append(product)


products = ["Pen", "Book"]

add_product(products, "Bag")

print(products)
```

Output:

```text
['Pen', 'Book', 'Bag']
```

Even though the function does not return the list, the original list is modified.

### 3. Modifying an existing list versus returning a new list

**Modifying an existing list** changes the original list object.

```python
def add_item(items, item):
    items.append(item)
    return items
```

This is useful when I intentionally want a function to update shared data, such as adding a product to the current inventory.

**Returning a new list** creates a separate list and leaves the original list unchanged.

```python
def add_item(items, item):
    new_items = items.copy()
    new_items.append(item)
    return new_items


products = ["Pen", "Book"]

result = add_item(products, "Bag")

print(products)
print(result)
```

Output:

```text
['Pen', 'Book']
['Pen', 'Book', 'Bag']
```

Here, `.copy()` creates a new list containing the same elements. The new item is appended to the copy, not to the original list.

### 4. When is modifying the original data useful?

Modifying the original list is useful when I want to update the existing data directly.

For example, in an inventory management system, I may want to add a product to the current product list or reduce a product's quantity after recording a sale.

This avoids creating a new list every time the inventory changes.

### 5. When can modifying the original data cause problems?

It can cause unexpected problems when another part of the program also uses the same list.

For example, if a function removes products from a list that another function depends on, the second function may receive unexpected data.

It can also make debugging harder because a function may change data without the caller realizing it.

Using a copy is helpful when I need to preserve the original data.

**Conclusion:** Lists are mutable, so modifying a list inside a function can affect the original list. If I want to preserve the original data, I can create a copy, modify that copy, and return it. I should choose between these approaches based on whether changing the original data is intentional.
