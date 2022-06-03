portion_down_payment = 0.25 #percentage of total_cost of home to be paid as down payment
r = 0.04  #annual rate of return on savings 

annual_salary = float(input("Enter your annual salary: "))
semi_annual_raise = float(input("Enter the semi annual raise as a decimal"))
total_cost = float(input("Enter the cost of your dream home: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

monthly_salary = annual_salary/12
monthly_return = r/12
down_payment = portion_down_payment * total_cost

months = 0
current_savings = 0

while current_savings <= down_payment:
    for month in range(months):
        if month == 6:
            monthly_salary += semi_annual_raise*monthly_salary
        
    current_savings += portion_saved*monthly_salary + current_savings*monthly_return
    months += 1
    
print('Number of months: %s months'
     % (months))