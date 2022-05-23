print("Welcome to the tip calculator")

bill = input("What was the total bill ? $")

tip_percentage = input("What percentage would you like to tip? 10, 12 0r 15?")

people = input("How many people would split the bill?")


tip_percent = int(tip_percentage)/100
total_tip = int(bill)*int(tip_percent)

total_bill = int(bill) + int(tip_percent)
bill_per_person = int(total_bill)/ int(people)

final_amount = round(bill_per_person, 2)
final_amount= "{:.2f}".format(bill_per_person)


print(f"Each person has to pay {final_amount}")

'''
"{:.2f}" - format specifier and place holder for floating points
'''
