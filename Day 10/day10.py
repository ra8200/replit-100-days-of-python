print("What was the bill?: ")
myBill = float(input())
print()
print("How many people?: ")
numberOfPeople = int(input())
answer = myBill / numberOfPeople
print()
print("What percentage would you like to tip: 15, 18, 20 percent?: ")
tip = int(input())
print()

bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)

print("You all owe", final_amount)
