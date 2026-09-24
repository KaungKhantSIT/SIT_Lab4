#Input prompt, input validation, and return valid integer/"quit" signal
def get_valid_input():
    stock = input("Enter stock quantity (or type 'quit' to exit): ")
    if stock.lower() == "quit":
        return "quit"
    try:
        stock = int(stock)
        if stock < 0:
            print("Please enter a positive number.")
            return None
        return stock
    except ValueError:
        print("Please enter a valid number.")
        return None

#Calculates & returns running total 
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

#Takes delivery amt & returns tax
def calculate_tax(amount):
    tax_rate = 0.1  # 10% tax rate
    taxed_total = amount * tax_rate
    return taxed_total

#Generate report of total units processed & failed entries
def generate_report(total_units, failed_attempts):
    report = f"Total Units Processed: {total_units}\n\
Number of Failed/Rejected Entries: {failed_attempts}"
    return report

#Auditor main program function
def auditor():
    total = 0
    failed = 0
    while True:
        user_input = get_valid_input()
        if user_input == "quit":
            print(generate_report(total, failed))
            break
        elif user_input is None:
            failed += 1
        else:
            total = process_delivery(total, user_input)
            if total > 500:
                print("Alert: Total Inventory exceeds 500 units.")
                print(generate_report(total, failed))
                break

#Run main program
auditor()