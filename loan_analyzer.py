import csv
from pathlib import Path


"""Part 1: Use Python to Automate Calculation of Data"""

loan_costs = [500, 600, 200, 1000, 450]

#counting the number of loans in the list using the len() function
number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} loans in the list")

#calculating the sum of the loans in the list using the sum() function
loans_total = sum(loan_costs)
print(f"The total value of all the loans is ${round(loans_total, 2)}")

#using defined variables to calculate average loan amount
average_loan_amount = loans_total / number_of_loans
print(f"The average loan value in the list is ${round(average_loan_amount, 2)}")


"""Part 2: Analyze Loan Data"""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#using get() function to extract data from the dictionary
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The future value of the loan is ${future_value}")
print(f"There are {remaining_months} months remaining on the loan")

#using the present value formula to store the fair value of the above loan
present_value = future_value / (1 + (0.2 / 12)) ** remaining_months

loan_price = loan.get("loan_price")

#using conditional if-then statement to determine if the loan is a good buy
if present_value >= loan_price:
    print("This loan is worth at least the cost to buy it!")
else:
    print("This loan is too expensive and not worth the price!")
print(f"The fair value is ${round(present_value, 2)}")


"""Part 3: Perform Financial Calculations"""

#defing a function that will calculate the present value (fair value) of any loan
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
    print(f"The present value of this loan is ${round(present_value, 2)}")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

annual_discount_rate = 0.2

#using the newly defined function to analyze data in the dictionary above
calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)


"""Part 4: Conditionally filter lists of loans"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#making an empty list that data can be added to
inexpensive_loans = []

#using a for loop to find the loans less than or equal to $500 in value and add them to the empty list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

print(inexpensive_loans)


"""Part 5: Save the results"""

#making a header fot the CSV file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

#creating a path for CSV fiel
output_path = Path("inexpensive_loans.csv")

#using a with-open function to write data from for loop into new CSV file
with open(output_path, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())