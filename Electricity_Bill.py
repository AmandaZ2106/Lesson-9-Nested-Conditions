units=int(input("Please entered the units you consumed:"))
if units<=50:
    amount=units*0.3
    surcharge=23
elif units<=100:
    amount=units*60
    surcharge=46
elif units<=160:
    amount=100+(units*60)  
    surcharge=50  
elif units<=200:
    amount=200+(units*60)
    surcharge=67
else:
    amount=246+(units*60)
    surcharge=78
Tot_amount=amount+surcharge    
print("Electricity Bill:",Tot_amount,"$")