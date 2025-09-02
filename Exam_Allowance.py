print("Answer the questions!")
Medical=input("Did you have a medical condition? Yes or No?")
if Medical=="Yes" or Medical=="yes":
    print("Allowed")
else:
    Attendance=float(input("Enter your attendance:"))
    if Attendance>=75:
        print("Allowed")
    else:
        print("Not Allowed!")    
        