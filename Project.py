Age=int(input("Enter your age:"))
if Age>=10 and Age<=20:
    print("You can join my class")
elif Age<10:
    Difference=10-Age
    print("Sorry, try again",Difference,"years later")
elif Age>20:
    print("You are over the age limit.Sorry!")   