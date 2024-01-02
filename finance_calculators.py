import math

# this program calculates the users investment or bond rates
# the user inputs their selection to be calculated
WANT_BOND = "bond"

WANT_INVEST = "investment"

WANT_SIMPLE = "simple"

WANT_COMPOUND = "compound"

print("""investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you will have to pay on your home loan
""")
# while loop chosen to ensure suitable user input before proceeding
while True:
    user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    user_choice = user_choice.lower()
    if user_choice == WANT_BOND:
        break
    if user_choice == WANT_INVEST:
        break
    print("That is not recognised.")

# bond calculation
if user_choice == WANT_BOND:
    house_value = int(input("please enter the present value of the house: "))
    interest_bond = int(input("please enter the interest rate: "))
    months_pay = int(input("please enter the number of months to repay the loan: "))
    interest_bond = (interest_bond / 100)/12
    repayment = (interest_bond * house_value)/(1 - (1 + interest_bond)**(-months_pay))
    print(f"your monthly repayment will be £{repayment}")
    exit()

# investment calculation
if user_choice == WANT_INVEST:
    deposit = int(input("please enter the amount you are depositing: "))
    interest_rate = int(input("please enter the interest rate: "))
    interest_rate = (interest_rate / 100)
    years_invest = int(input("please enter the number of years you are investing: "))
    interest = input("please enter either 'simple' or 'compound' interest: ")
    interest = interest.lower()

if interest == WANT_SIMPLE:
    total_simple = deposit *(1 + interest_rate*years_invest)
    print(f"your total interest will amount to £{total_simple}")

if interest == WANT_COMPOUND:
    total_compound = deposit * math.pow((1+interest_rate),years_invest)
    print(f"your total interest will amount to £{total_compound}")



















