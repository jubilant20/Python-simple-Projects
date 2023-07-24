#This tip calculator makes it convenient for users to quickly determine the individual share, promoting transparency and ease in settling bills when dining in groups.

print("Welcome to the tip calculator!")
print("______________________________\n")

bill=float(input("What was the total bill? $"))

tip=int(input("What percentage tip would you like to give?\n10,12 or 15? "))
 
s_bill=int(input("How many people to split the bill? "))

tip_per=tip/100
total_tip=bill*tip_per
total_bill=bill+total_tip
bill_per_person=total_bill/s_bill
final_amt=round(bill_per_person, 2)
print(f"Each person should pay: ${final_amt}")