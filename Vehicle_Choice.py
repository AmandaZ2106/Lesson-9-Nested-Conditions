print("1.Car\n2.Bike")
C1=int(input("Enter your choice:"))
if C1==1:
    print("1.XUV\n2.Sedan")
    C1a=int(input("Enter your choice:"))
    if C1a==1:
        print("You have selcted an XUV")
    elif C1a==2:
        print("You have selected a sedan!")
    else:
        print("Wrong Choice")   
elif C1==2:
    print("1.Scooty\n2.Bullet")
    C2a=int(input("Enter your choice:"))
    if C2a==1:
        print("You have selcted a Scooty")
    elif C2a==2:
        print("You have selected a Bullet!")
    else:
        print("Wrong Choice")
else:
    print("Wrong Choice!")            

            

     
  