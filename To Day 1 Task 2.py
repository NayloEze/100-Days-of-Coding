portion_down_payment = 0.25 #percentage of total_cost of home to be paid as down payment
r = 0.04  #annual rate of return on savings 

annual_salary = float(input("Enter your annual salary: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

monthly_return = r/12 #annual rate of return divided by 12
down_payment = portion_down_payment * total_cost #calculation of down_payment

months = 0
current_savings = 0

while current_savings <= down_payment:
    current_savings += portion_saved*(annual_salary/12) + current_savings*monthly_return #amount saved every month + monthly returns
    months += 1
    
print('Number of months: %s months'
     % (months))
