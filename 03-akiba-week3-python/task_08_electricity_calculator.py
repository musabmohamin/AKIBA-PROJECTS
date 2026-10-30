
def validate_units(units):
    if units < 0:
        return False
    else:
        return True

def calculate_tier_charge(units):
    if units <= 50:
        charge = units * 0.50
    elif units <= 150:
        charge = (50 * 0.50) + ((units - 50) * 0.75)
    else:
        charge = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)

    return charge

def calculate_bill(units, service_fee=0):
    charge = calculate_tier_charge(units)
    total_bill = charge + service_fee
    return total_bill

def generate_bill_summary(units):
    if not validate_units(units):
        return "Invalid electricity units."

    charge = calculate_tier_charge(units)
    total_bill = calculate_bill(units)

    summary = f"""
    ELECTRICITY BILL
    ----------------
    Units consumed: {units}
    Electricity charge: {charge:.2f} Birr
    Total bill: {total_bill:.2f} Birr
    service fee: 0.00 Birr
    """

    return summary

units = float(input("Enter electricity units consumed: "))

if validate_units(units):
    print(generate_bill_summary(units))
else:
    print("Invalid input. Units cannot be negative.")