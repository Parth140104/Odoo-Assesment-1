# Slab Rates:

# 0-100 kWh @ ₹5/unit

# 101-300 kWh @ ₹7/unit

# 301-500 kWh @ ₹10/unit

# Above 500 kWh @ ₹15/unit

# For each slab, we calculate the charge by multiplying the number of units in that slab by the rate and subtracting the units used from the total.

def calculate_electricity_bill(usage):
    slabs = [
        (100, 5),   
        (200, 7),   
        (200, 10),  
        (float('inf'), 15)  
    ]

    total_amount = 0
    remaining_usage = usage
    print("Electricity Bill:")
    
    for slab, rate in slabs:
        if remaining_usage > 0:
            if remaining_usage <= slab:
                charge = remaining_usage * rate
                print(f"{usage - remaining_usage + 1}-{usage - remaining_usage + remaining_usage} units @ ₹{rate}/unit = {charge}₹")
                total_amount += charge
                break
            else:
                charge = slab * rate
                print(f"{usage - remaining_usage + 1}-{usage - remaining_usage + slab} units @ ₹{rate}/unit = {charge}₹")
                total_amount += charge
                remaining_usage -= slab

    print(f"Total Amount Payable = {total_amount}₹")

usage = int(input("Enter electricity usage (in kWh): "))

calculate_electricity_bill(usage)
