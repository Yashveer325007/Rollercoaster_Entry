print("Welcome to the Rollercoaster")
height=int(input("Enter your height in cm\n"))
if (height>=120):
  print("You can ride")
  age=int(input("Enter your age\n"))
  if age<12:
    print("You have to pay 10 rupees")
  elif (age>12 & age<18):
    print("You have to pay 25 rupees")
  else:
    print("You have to pay 50 rupees")
else:
  print("Sorry, You cannot ride as your height is less then 120")
  
