# python program on leap year using conditional statements and logical operators

#Taking input from the user
year = int(input("Enter a year:"))
if(year%4==0 and year%100!=0) or year%400==0:
    print(year," is a Leap year")
else:
    print(year," is not a Leap year.")
    
