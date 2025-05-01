def fulfill_order(inventory, order, budget):

    # Sort inventory by price (cheapest first)
    inventory.sort(key=lambda x: x['price'])

    total_cost = 0
    purchased_items = {}

    for item in inventory:
        name, available_qty, unit_price = item['name'], item['quantity'], item['price']

        if name in order:
            needed_qty = order[name]
            purchasable_qty = min(needed_qty, available_qty)  # Max we can buy based on stock
            cost = purchasable_qty * unit_price

            if total_cost + cost <= budget:
                total_cost += cost
                purchased_items[name] = purchasable_qty
                order[name] -= purchasable_qty  # Reduce required amount

    # Check fulfillment status
    if all(qty == 0 for qty in order.values()):
        return f" Fully fulfillable. Purchased: {purchased_items}. Total cost: ${total_cost}"
    
    if total_cost > 0:
        return f" Partially fulfillable. Purchased: {purchased_items}. Spent: ${total_cost}, Remaining budget: ${budget - total_cost}"
    
    return " Order impossible within budget."

# --- Example Input ---
inventory = [
    {'name': 'Laptop', 'quantity': 5, 'price': 1000},
    {'name': 'Mouse', 'quantity': 10, 'price': 20},
    {'name': 'Keyboard', 'quantity': 8, 'price': 50}
]

order = {'Laptop': 2, 'Mouse': 3, 'Keyboard': 2}
budget = 1200

# --- Run the function ---
print(fulfill_order(inventory, order, budget))
