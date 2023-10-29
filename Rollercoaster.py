print("Welcome to the Rollercoaster")
bill=0
height=int(input("Enter your height in cm\n"))
if (height>=120):
  print("You can ride")
  age=int(input("Enter your age\n"))
  if age<12:
    bill=10
    print("You have to pay 10 rupees")
  elif (age>12 & age<18):
    bill=25
    print("You have to pay 25 rupees")
  else:
    bill=50
    print("You have to pay 50 rupees")

  wants_photo=input("Do you want a photo? Y or N \n")
  if (wants_photo=="Y"):
    bill=bill+3
  print(f"Your final bill is {bill}.")
  
else:
  print("Sorry, You cannot ride as your height is less then 120")
  
