import math

def annual_percentage_yield(principal, interest_rate, periods_per_year):
    """
    Calculate the annual percentage yield given the principal, 
    interest rate, and compounding periods per year.
    """
    apy = (1 + (interest_rate / periods_per_year)) ** periods_per_year - 1
    return apy

def balloon_loan_payment(principal, interest_rate, term):
    """
    Calculate the monthly payment for a balloon loan given the principal,
    interest rate, and term in months.
    """
    monthly_rate = interest_rate / 12
    payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -term))
    return payment

def compound_interest(principal, interest_rate, compounding_periods, years):
    """
    Calculate compound interest given principal, interest rate, 
    compounding periods per year, and number of years.
    """
    total_compounding_periods = compounding_periods * years
    return principal * (1 + (interest_rate / compounding_periods)) ** total_compounding_periods

def continuous_compounding(principal, interest_rate, years):
    """
    Calculate continuously compounded interest given principal, 
    interest rate, and number of years.    
    """
    return principal * math.exp(interest_rate * years) 

def debt_to_income_ratio(monthly_debt, monthly_income):
    """
    Calculate debt-to-income ratio given monthly debt and income.
    """  
    return monthly_debt / monthly_income

def balloon_balance(principal, interest_rate, term, months_elapsed):
    """
    Calculate the remaining balance on a balloon loan after making 
    payments over a given number of months.
    """
    monthly_rate = interest_rate / 12 
    remaining_payments = term - months_elapsed
    balance = principal * (1 + monthly_rate) ** remaining_payments
    return balance

def loan_payment(principal, interest_rate, term):
    """
    Calculate the monthly payment for a loan given the principal,
    interest rate, and term in months.
    """
    monthly_rate = interest_rate / 12
    payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -term))
    return payment

def balance_on_loan(principal, interest_rate, months_elapsed, monthly_payment):
    """
    Calculate the remaining balance on a loan after making monthly
    payments over a given number of months.
    """
    monthly_rate = interest_rate / 12
    balance = principal * (1 + monthly_rate) ** months_elapsed - \
              monthly_payment * (1 + monthly_rate) ** months_elapsed - 1 / monthly_rate
    return balance

def loan_to_deposit_ratio(total_loans, total_deposits):
    """
    Calculate the loan to deposit ratio for a bank given their total loans
    and total deposits.
    """
    return total_loans / total_deposits

def simple_interest(principal, interest_rate, years):
    """
    Calculate simple interest given principal, interest rate, and years.
    """
    return principal * interest_rate * years

def net_interest_income(interest_income, interest_expense):
    """
    Calculate net interest income given total interest income and total
    interest expense.
    """
    return interest_income - interest_expense

def loan_to_value(loan_amount, home_value):
    """
    Calculate loan-to-value ratio given the loan amount and home value.
    """
    return loan_amount / home_value

def calculate_future_value(principal, interest_rate, years):
    """
    Calculate the future value of an investment given principal,
    interest rate, and number of years.
    """
    return principal * (1 + interest_rate) ** years

def calculate_present_value(future_value, interest_rate, years):
    """
    Calculate the present value required to achieve a specific future value
    given an interest rate and number of years.
    """
    return future_value / (1 + interest_rate) ** years

def calculate_loan_affordability(monthly_income, monthly_expenses, interest_rate, term_in_years):
    """
    Calculate the maximum affordable loan amount based on monthly income,
    expenses, interest rate, and term in years.
    """
    monthly_payment = loan_payment(monthly_income - monthly_expenses, interest_rate, term_in_years * 12)
    return monthly_payment * term_in_years * 12

def calculate_savings_goal_amount(current_savings, monthly_contributions, interest_rate, years):
    """
    Calculate the target savings amount based on current savings, monthly contributions,
    interest rate, and number of years.
    """
    future_value = current_savings * (1 + interest_rate) ** years
    future_value += monthly_contributions * (math.pow(1 + interest_rate, years * 12) - 1) / (interest_rate / 12)
    return future_value

def calculate_credit_card_interest(principal, annual_interest_rate, monthly_payment):
    """
    Calculate the total interest paid on a credit card balance given
    the principal, annual interest rate, and monthly payment.
    """
    remaining_balance = principal
    total_interest = 0
    monthly_rate = annual_interest_rate / 12
    while remaining_balance > 0:
        interest_payment = remaining_balance * monthly_rate
        total_interest += interest_payment
        remaining_balance = max(0, remaining_balance - monthly_payment + interest_payment)
    return total_interest