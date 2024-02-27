month = ["January", "February", "March", "April", "May"]
expense = [5200, 6350, 4600, 4130, 3190]

print("\nIn Feb, how many pesos you spent extra compare to January?")
print(f"{month[1]} extra costs compared to {month[0]} is : {expense[1] - expense[0]}\n")

print("\nFind out your total expense in first quarter (first three months) of the year")
print(f"Total expenses in the third quarter is: {expense[0]+expense[1]+expense[2]}\n")

print("\nDid you spend exactly 2000 pesos in any month?")
for i in range(len(month)):
    if expense[i] != 2000:
        print(f"{month[i]} expense isn't 2000")
    elif expense[i] == 2000:
        print(f"{month[i]} expense is 2000")

print("\nUpdated expenses after June:")
new_month = "June"
new_expense = 1980
month.append(new_month)
expense.append(new_expense)

print(f"Updated Months: {month}")
print(f"Updated expenses: {expense}\n")

print("\nExpenses after refund correction in April:")
expense[3] -= 200
print(f"Updated Months: {month}")
print(f"Updated expenses: {expense}\n")
