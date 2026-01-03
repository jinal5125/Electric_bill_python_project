unit=int(input("Enter total unit:"))
peak_hour=int(input("enter peak hours:"))
late_payment=input("Is payment delayed? (y/n):")

while unit < 0:
    print("Negative number allowed nahi hai.")
    unit = int(input("Enter total unit again: "))

while peak_hour < 0:
    print("Negative number allowed nahi hai.")
    peak_hour = int(input("Enter peak hours again: "))


dis = 0
peakCharge = 0
penlty=0

if unit > 0 and unit <= 100:
       total = unit * 5 + 50
       print("Medium electricity consumption")
       if unit <= 50 and unit > 0:
               dis = total * 5 / 100
       print(f"Discount is : {dis}")
       print("Low electricity usage. Good job!")
elif unit == 0:
       print("No electricity consumption. Bill = ₹0")
elif unit>=101 and unit<=200:
        total=unit*7+50
        print(f"total bill is:{total}")
        print("Medium electricity consumption.")
elif unit>=201 and unit<=300:
        total=unit*10+50
        print(f"total bill is:{total}")
elif unit >=301:
        total=unit*15+50
        charge=total*10/100
        print(f"total charge is:{charge}")
        final=total+charge
        print(f"total bill with charge:{final}")
        print("High electricity usage! Try saving power.")

if peak_hour >= 50:
        peakCharge = (peak_hour - 50) * 2
        print(f"Peack hour is : {peakCharge}")
else:
    print(f"Peack hour is : {peakCharge}")


if late_payment=='y':
       penlty=100
else:
       print("No late payment penalty.")

final = total + peakCharge - dis + penlty


print("\n----------Final bill--------------")
print(f"total units:{unit}")
print(f"total Amount: ₹{total}")
print(f"Fixed Charge: ₹50")
print(f"Surcharge (if any): ₹{peakCharge}")
print(f"Discount: ₹{dis}")
print(f"Late Payment Penalty: ₹{penlty}")
print("------------------------------------")
print(f"Final Payable Amount: ₹{final}")
