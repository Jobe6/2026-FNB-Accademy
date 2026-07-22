contacts = [
    {"Name" : "Sizwe","Phone" : "079536263"},
    {"Name" : "Sihle", "Phone" : "084574387"},
    {"Name" : "Senzo", "Phone" : "045978343"}
    ]
    
search = input("Enter the name you are looking for : ")

for contact in contacts:
    if search == contact["Name"]:
        print(f"Found! " + contact["Name"] + "'s" + " number is " + contact["Phone"])
        break
    else:
       print("Contact not found!!")