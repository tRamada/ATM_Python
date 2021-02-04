def Menu():
    print("\n\n\nWelcome to tRamada ATM\n")
    print("1 - Create Account")
    print("2 - Login")
    print("3 - Exit")
    return input("\nChose: ")

#Dicionary to save Create Account infos
user = {
    "Name":"",
    "Adress":"",
    "BI Number":"",
    "Password":""
}

# Create Account and Login
def Decison(awnser,user):
    if int(awnser) == 1:
        print("\n\n\nLooks like you are new here! \nLet's get your fisrt ATM account!\n")
        user["Name"] = input("Insert your name: ")
        user["Adress"] = input("Now, Write your address: ")
        user["BI Number"] = input("Your BI number: ")
        user["Password"] = input("All infos is collected. Now chose 3 numbers to be your login password: ")
        print("\nYour account has been created! Chose Login to get inside your account.")
    elif int(awnser) == 2:
        password_login = input("Insert your password: ")
        if password_login == user["Password"]:
            IntoLogin()
    return user

#Login Menu
def IntoLogin():
    print("----*Name* Banco----\n")
    print("1 - Consult balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")
    return input("\nChose: ")

while True:
    awnser = Menu()
    user = Decison(awnser,user)
    
    