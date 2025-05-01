def record_transactions():
    transactions = []
    balance = 0

    print("Enter your transactions (e.g., credit 500 or debit 200). Type 'done' to finish.\n")

    while True:
        entry = input("Transaction: ").strip().lower()
        if entry == 'done':
            break

        try:
            parts = entry.split()
            if len(parts) != 2:
                raise ValueError

            action, amount_str = parts
            amount = float(amount_str)

            if action not in ['credit', 'debit']:
                raise ValueError

            if amount < 0:
                raise ValueError

            if action == 'credit':
                balance += amount
                transactions.append((action.capitalize(), amount, balance))
            elif action == 'debit':
                balance -= amount
                transactions.append((action.capitalize(), -amount, balance))

            print(f"✅ {action.capitalize()} of ₹{amount:.2f}. Current Balance: ₹{balance:.2f}")

        except ValueError:
            print("❌ Invalid input. Please enter in the format 'credit 100' or 'debit 50'.")

    # Final Summary
    print("\n--- Transaction Summary ---")
    print(f"{'Type':<10}{'Amount':>10}{'Balance':>15}")
    print("-" * 35)
    for t_type, t_amount, t_balance in transactions:
        print(f"{t_type:<10}{t_amount:>10.2f}{t_balance:>15.2f}")
    print("-" * 35)
    print(f"{'Final Balance':<20}: ₹{balance:.2f}")

# Run the function
record_transactions()
