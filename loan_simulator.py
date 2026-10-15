
loan_amount = float(input("Enter loan amount: $"))
annual_rate = float(input("Enter annual interest rate (%): "))
monthly_payment = float(input("Enter monthly payment: $"))

monthly_rate = annual_rate / 100 / 12
balance = loan_amount
months = 0

if loan_amount <= 0 or monthly_payment <= 0 or annual_rate < 0:
    print("Please enter valid loan details.")
elif monthly_rate > 0 and monthly_payment <= balance * monthly_rate:
    print("Payment is too small to pay off the loan.")
else:
    while balance > 0:
        interest = balance * monthly_rate
        balance = balance + interest
        balance = balance - monthly_payment
        months = months + 1

        if balance < 0:
            balance = 0

    print("Loan paid off in", months, "months.")