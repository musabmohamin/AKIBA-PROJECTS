#Project management module

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

    

def add_product(products):
    while 1:
        product_add=input("Enter product name:")
        
        error=validator(product_add,"name")
        if error is not None:
            print(error)
            continue
        quantity_add=int(input("Enter quantity to add:"))
        error=validator(quantity_add,"quantity")
        if error is not None:
            print(error)
            continue
        price_add=int(input("Enter the price of the product :"))
        error=validator(price_add,"price")
        if error is not None:
            print(error)
            continue
        for product in products:
            if product["name"]==product_add:
                product["quantity"]=product["quantity"]+quantity_add
        
        products.append({"name": product_add,"price":price_add,"quantity":quantity_add})
       
        add=input("Enter 1 to add another product 0 to exit from add product:")
        error=validator(add,"option add")
        if error is not None:
            print(error)
            continue
        add=int(add)
        
        if add==1:
            continue
        elif add==0:
            break
        else:
            return "Enter 0 or 1"
            
    return products



def search_product(products):
    product_search=input("Enter the product name to search:")
    validator(product_search,"name")
    for product in products:
        if product["name"].lower()==product_search.lower():
            return product
        else:
            return "there is no product with such name"


def update_product_info(products):
    product_update=input("Enter product name to update :")
    validator(product_update,"name")
    choose=int(input("ENTER 1 to update product price or 2 to update product quantity :"))
    if choose==1:
        for product in products:
            if product["name"].lower()==product_update.lower():
                price_update=int(input("Enter the product updated price:"))
                validator(price_update,"price")
                product["price"]=price_update
            return products
        else:
            return "There is no product with this name "
    elif choose==2:
        for product in products:
            if product["name"].lower()==product_update.lower():
                quantity_update=int(input("Enter the product updated quantity:"))
                validator(quantity_update,"quantity")
                product["quantity"]=quantity_update
                return  products
        else:
            return "There is no product with this name "
            
def display(products):
    return products


    



       

    