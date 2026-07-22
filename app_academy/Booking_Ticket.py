print("To book your SHOW Ticket, provide your details below  \n")

Last_name = input("Enter your Last Name : ")
First_name = input("Enter your First Name(s) : ")
contact_number = int(input("Enter your Contact number : "))
Artist_name = input("Which Band/Artist do you want to see : ")

print("\n")

print(f"Congratulations " + Last_name.upper() + " " + 
      First_name.upper() + " " + f"with contact nummber " 
      + str(contact_number) + f" on your booking to see " + Artist_name.upper()
      )

