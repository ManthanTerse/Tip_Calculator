#Project 2 : Tip Calculator 

def tip_calculator():
    print("Tip Calculator")

    try:
        bill = float(input("Enter the total bill amount (₹): "))
        tip_percent = float(input("Enter tip percentage (e.g., 10, 15, 20): "))
        people = int(input("Enter number of people splitting the bill: "))

        if bill < 0 or tip_percent < 0 or people <= 0:
            print(" Please enter positive values.")
            return

        tip_amount = (tip_percent / 100) * bill
        total_bill = bill + tip_amount
        per_person = total_bill / people

        print("\n--- Tip Calculation ---")
        print(f"Original Bill: ₹{bill:.2f}")
        print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
        print(f"Total Bill (with tip): ₹{total_bill:.2f}")
        print(f"Each person pays: ₹{per_person:.2f}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

tip_calculator()

